from __future__ import annotations

from collections.abc import AsyncGenerator
from typing import Any

import pytest

from vkapi import Bot, Dispatcher
from vkapi.client.session.base import BaseSession
from vkapi.filters import Command
from vkapi.fsm import FSMContext, FSMStrategy, State, StateFilter, StatesGroup
from vkapi.fsm.storage.redis import RedisStorage
from vkapi.methods.base import MethodT
from vkapi.types import Message


class FakeSession(BaseSession):
    async def close(self) -> None:
        pass

    async def make_request(
        self,
        bot: Bot,
        method: MethodT[Any],
        timeout: float | None = None,
    ) -> Any:
        return {}

    async def stream_content(
        self,
        url: str,
        *,
        timeout: float = 30.0,
        chunk_size: int = 65536,
    ) -> AsyncGenerator[bytes, None]:
        yield b""


class Form(StatesGroup):
    name = State()
    age = State()


def raw_message(text: str, *, peer_id: int = 2_000_000_001, from_id: int = 42) -> dict[str, Any]:
    return {
        "type": "message_new",
        "group_id": 1,
        "object": {
            "message": {
                "id": 10,
                "conversation_message_id": 5,
                "peer_id": peer_id,
                "from_id": from_id,
                "text": text,
            },
        },
    }


def test_states_group_binds_stable_state_names() -> None:
    assert Form.name.state == "Form:name"
    assert str(Form.age) == "Form:age"
    assert Form.__states__ == (Form.name, Form.age)


@pytest.mark.asyncio
async def test_dispatcher_routes_by_state_filter_and_injects_context() -> None:
    bot = Bot("token", group_id=1, session=FakeSession(), rate_limit=None)
    dp = Dispatcher()
    hits: list[tuple[str, dict[str, Any]]] = []

    @dp.message(Command("start"))
    async def start(message: Message, state: FSMContext) -> None:
        await state.set_state(Form.name)
        hits.append(("start", {"text": message.text}))

    @dp.message(StateFilter(Form.name))
    async def name(message: Message, state: FSMContext) -> None:
        data = await state.update_data(name=message.text)
        await state.set_state(Form.age)
        hits.append(("name", data))

    @dp.message(StateFilter(Form.age))
    async def age(message: Message, state: FSMContext) -> None:
        data = await state.get_data()
        await state.clear()
        hits.append(("age", {**data, "age": message.text}))

    await dp.feed_update(bot, raw_message("/start"))
    await dp.feed_update(bot, raw_message("Alice"))
    await dp.feed_update(bot, raw_message("30"))
    await dp.feed_update(bot, raw_message("ignored"))

    assert hits == [
        ("start", {"text": "/start"}),
        ("name", {"name": "Alice"}),
        ("age", {"name": "Alice", "age": "30"}),
    ]


@pytest.mark.asyncio
async def test_fsm_user_in_peer_strategy_isolates_same_user_in_different_peers() -> None:
    bot = Bot("token", group_id=1, session=FakeSession(), rate_limit=None)
    dp = Dispatcher(fsm_strategy=FSMStrategy.USER_IN_PEER)
    hits: list[str] = []

    @dp.message(Command("start"))
    async def start(state: FSMContext) -> None:
        await state.set_state(Form.name)

    @dp.message(StateFilter(Form.name))
    async def name(message: Message, state: FSMContext) -> None:
        await state.clear()
        hits.append(message.text)

    await dp.feed_update(bot, raw_message("/start", peer_id=100, from_id=42))
    await dp.feed_update(bot, raw_message("wrong peer", peer_id=200, from_id=42))
    await dp.feed_update(bot, raw_message("right peer", peer_id=100, from_id=42))

    assert hits == ["right peer"]


@pytest.mark.asyncio
async def test_state_filter_none_matches_absent_state() -> None:
    bot = Bot("token", group_id=1, session=FakeSession(), rate_limit=None)
    dp = Dispatcher()
    hits: list[str] = []

    @dp.message(StateFilter(None))
    async def no_state(message: Message) -> None:
        hits.append(message.text)

    await dp.feed_update(bot, raw_message("free"))

    assert hits == ["free"]


class FakeRedis:
    def __init__(self) -> None:
        self.values: dict[str, str] = {}
        self.closed = False

    async def get(self, key: str) -> str | None:
        return self.values.get(key)

    async def set(self, key: str, value: str, **kwargs: Any) -> None:
        self.values[key] = value

    async def delete(self, key: str) -> None:
        self.values.pop(key, None)

    async def aclose(self) -> None:
        self.closed = True


@pytest.mark.asyncio
async def test_redis_storage_uses_client_without_requiring_redis_server() -> None:
    client = FakeRedis()
    storage = RedisStorage(client)
    dp = Dispatcher(storage=storage)
    bot = Bot("token", group_id=1, session=FakeSession(), rate_limit=None)
    seen: list[dict[str, Any]] = []

    @dp.message(Command("start"))
    async def start(state: FSMContext) -> None:
        await state.set_state(Form.name)
        await state.update_data(step=1)

    @dp.message(StateFilter(Form.name))
    async def name(message: Message, state: FSMContext) -> None:
        seen.append(await state.update_data(name=message.text))
        await state.clear()

    await dp.feed_update(bot, raw_message("/start"))
    await dp.feed_update(bot, raw_message("Alice"))
    await storage.close()

    assert seen == [{"step": 1, "name": "Alice"}]
    assert client.values == {}
    assert client.closed is True
