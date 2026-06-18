from __future__ import annotations

from typing import Any

import pytest

from vkapi import Bot, Depends, Dispatcher, Router
from vkapi.client.session.base import BaseSession
from vkapi.filters import Command, F, Payload, PeerType, Text
from vkapi.methods.base import VKMethod
from vkapi.types import Message, Update


class FakeSession(BaseSession):
    async def close(self) -> None:
        pass

    async def make_request(
        self,
        bot: Bot,
        method: VKMethod[Any],
        timeout: float | None = None,
    ) -> Any:
        return {}

    async def stream_content(self, url: str, *, timeout: float = 30.0, chunk_size: int = 65536):
        if False:
            yield b""


def raw_message(text: str = "/start", payload: str | None = None) -> dict[str, Any]:
    message: dict[str, Any] = {
        "id": 10,
        "conversation_message_id": 5,
        "peer_id": 2_000_000_001,
        "from_id": 42,
        "text": text,
    }
    if payload is not None:
        message["payload"] = payload
    return {"type": "message_new", "group_id": 1, "object": {"message": message}}


@pytest.mark.asyncio
async def test_dispatcher_routes_message_with_di_and_filters() -> None:
    bot = Bot("token", group_id=1, session=FakeSession(), rate_limit=None)
    dp = Dispatcher()
    router = Router()
    seen: list[tuple[str, Bot, str]] = []

    def get_label() -> str:
        return "dep"

    @router.message(Command("start"), PeerType("chat"))
    async def handler(message: Message, bot: Bot, label: str = Depends(get_label)) -> None:
        seen.append((message.text, bot, label))

    dp.include_router(router)

    await dp.feed_update(bot, raw_message())

    assert seen == [("/start", bot, "dep")]


@pytest.mark.asyncio
async def test_filters_text_payload_and_magic() -> None:
    bot = Bot("token", group_id=1, session=FakeSession(), rate_limit=None)
    dp = Dispatcher()
    hits: list[str] = []

    @dp.message(Text(contains="hello"), Payload(action="go"), F.text.startswith("hello"))
    async def handler(message: Message) -> None:
        hits.append(message.text)

    await dp.feed_update(bot, raw_message("hello world", '{"action":"go"}'))
    await dp.feed_update(bot, raw_message("hello world", '{"action":"stop"}'))

    assert hits == ["hello world"]


@pytest.mark.asyncio
async def test_polling_processes_fake_updates() -> None:
    bot = Bot("token", group_id=1, session=FakeSession(), rate_limit=None)
    dp = Dispatcher()
    hits: list[str] = []

    async def listen(bot: Bot, **kwargs: Any):
        yield Update.model_validate(raw_message("one"))
        dp.stop_polling()

    dp._listen_updates = listen  # type: ignore[method-assign]

    @dp.message()
    async def handler(message: Message) -> None:
        hits.append(message.text)

    await dp.start_polling(bot, handle_as_tasks=False, handle_signals=False)

    assert hits == ["one"]
