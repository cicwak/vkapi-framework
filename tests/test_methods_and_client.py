from __future__ import annotations

from collections.abc import AsyncGenerator
from pathlib import Path
from typing import Any, cast

import pytest

from vkapi import Bot
from vkapi.client.session.base import BaseSession
from vkapi.exceptions import (
    VKAccessDeniedError,
    VKAPIResponseError,
    VKDecodeError,
    VKRateLimitError,
)
from vkapi.methods import MessagesSend
from vkapi.methods.base import MethodT
from vkapi.upload import Upload


class FakeSession(BaseSession):
    def __init__(self, result: Any = None) -> None:
        super().__init__()
        self.result = result
        self.calls: list[tuple[str, dict[str, Any]]] = []

    async def close(self) -> None:
        pass

    async def make_request(
        self,
        bot: Bot,
        method: MethodT[Any],
        timeout: float | None = None,
    ) -> Any:
        self.calls.append((method.__api_method__, self.prepare_params(bot, method)))
        return self.result

    async def stream_content(
        self,
        url: str,
        *,
        timeout: float = 30.0,
        chunk_size: int = 65536,
    ) -> AsyncGenerator[bytes, None]:
        yield b""


class FakeUploadBot:
    def __init__(self, responses: list[Any]) -> None:
        self.responses = responses
        self.calls: list[tuple[str, dict[str, Any]]] = []

    async def api(self, method: str, **params: Any) -> Any:
        self.calls.append((method, params))
        return self.responses.pop(0)


class FakeUpload(Upload):
    def __init__(self, bot: FakeUploadBot, upload_response: dict[str, Any]) -> None:
        super().__init__(cast(Bot, bot))
        self.upload_response = upload_response
        self.post_calls: list[tuple[str, str, Path]] = []

    async def _post_file(self, upload_url: str, field: str, path: str | Path) -> dict[str, Any]:
        self.post_calls.append((upload_url, field, Path(path)))
        return self.upload_response


def test_generated_method_serialization() -> None:
    method = MessagesSend(peer_id=1, random_id=0, message="hi")

    assert method.__api_method__ == "messages.send"
    assert method.build_request() == {"peer_id": 1, "random_id": 0, "message": "hi"}


@pytest.mark.asyncio
async def test_bot_namespace_uses_generated_method() -> None:
    session = FakeSession(result=123)
    bot = Bot("token", group_id=1, session=session, rate_limit=None)

    result = await bot.messages.send(peer_id=1, random_id=0, message="hi")

    assert result == 123
    assert session.calls == [
        (
            "messages.send",
            {
                "access_token": "token",
                "v": "5.199",
                "peer_id": 1,
                "random_id": 0,
                "message": "hi",
            },
        ),
    ]


@pytest.mark.asyncio
async def test_bot_raw_api_is_not_overridden_by_generated_execute_namespace() -> None:
    session = FakeSession(result={"ok": True})
    bot = Bot("token", group_id=1, session=session, rate_limit=None)

    result = await bot.api("execute", code="return 1;")

    assert result == {"ok": True}
    assert session.calls == [
        (
            "execute",
            {"access_token": "token", "v": "5.199", "code": "return 1;"},
        ),
    ]


@pytest.mark.asyncio
async def test_bot_send_message_uses_raw_api_helper() -> None:
    session = FakeSession(result=321)
    bot = Bot("token", group_id=1, session=session, rate_limit=None)

    result = await bot.send_message(peer_id=1, random_id=0, message="hi")

    assert result == 321
    assert session.calls == [
        (
            "messages.send",
            {"access_token": "token", "v": "5.199", "peer_id": 1, "random_id": 0, "message": "hi"},
        ),
    ]


def test_check_response_maps_errors() -> None:
    session = FakeSession()

    with pytest.raises(VKRateLimitError):
        session.check_response("users.get", '{"error":{"error_code":6,"error_msg":"too many"}}')

    with pytest.raises(VKAccessDeniedError):
        session.check_response("users.get", '{"error":{"error_code":15,"error_msg":"denied"}}')


def test_check_response_returns_response_payload() -> None:
    session = FakeSession()

    result = session.check_response("users.get", '{"response":{"id":1,"name":"Ada"}}')

    assert result == {"id": 1, "name": "Ada"}


def test_check_response_rejects_invalid_payloads() -> None:
    session = FakeSession()

    with pytest.raises(VKDecodeError):
        session.check_response("users.get", "[]")

    with pytest.raises(VKDecodeError):
        session.check_response("users.get", '{"error":"broken"}')

    with pytest.raises(VKDecodeError):
        session.check_response("users.get", '{"ok":true}')


def test_check_response_filters_non_mapping_request_params() -> None:
    session = FakeSession()

    with pytest.raises(VKAPIResponseError) as exc_info:
        session.check_response(
            "users.get",
            (
                '{"error":{"error_code":100,"error_msg":"bad",'
                '"request_params":[{"key":"user_id","value":"1"},"skip",5]}}'
            ),
        )

    assert exc_info.value.request_params == [{"key": "user_id", "value": "1"}]


@pytest.mark.asyncio
async def test_upload_message_photo_builds_attachment_from_saved_photo() -> None:
    bot = FakeUploadBot(
        [
            {"upload_url": "https://upload.example/photo"},
            [{"owner_id": 10, "id": 20}],
        ],
    )
    upload = FakeUpload(bot, {"photo": "raw-photo", "server": 1, "hash": "hash"})

    attachment = await upload.message_photo(123, "photo.jpg")

    assert attachment == "photo10_20"
    assert bot.calls == [
        ("photos.getMessagesUploadServer", {"peer_id": 123}),
        (
            "photos.saveMessagesPhoto",
            {"photo": "raw-photo", "server": 1, "hash": "hash"},
        ),
    ]
    assert upload.post_calls == [("https://upload.example/photo", "photo", Path("photo.jpg"))]


@pytest.mark.asyncio
async def test_upload_doc_builds_attachment_from_doc_response() -> None:
    bot = FakeUploadBot(
        [
            {"upload_url": "https://upload.example/doc"},
            {"doc": {"owner_id": 30, "id": 40}},
        ],
    )
    upload = FakeUpload(bot, {"file": "uploaded-file"})

    attachment = await upload.doc(456, "file.txt")

    assert attachment == "doc30_40"
    assert bot.calls == [
        ("docs.getMessagesUploadServer", {"peer_id": 456, "type": "doc"}),
        ("docs.save", {"file": "uploaded-file"}),
    ]
    assert upload.post_calls == [("https://upload.example/doc", "file", Path("file.txt"))]
