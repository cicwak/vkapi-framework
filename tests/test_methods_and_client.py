from __future__ import annotations

from collections.abc import AsyncGenerator
from typing import Any

import pytest

from vkapi import Bot
from vkapi.client.session.base import BaseSession
from vkapi.exceptions import VKAccessDeniedError, VKRateLimitError
from vkapi.methods import MessagesSend
from vkapi.methods.base import MethodT


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
