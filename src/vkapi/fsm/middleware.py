from __future__ import annotations

from collections.abc import Awaitable, Callable
from typing import Any

from vkapi.client.bot import Bot

from .context import FSMContext
from .storage.base import BaseStorage, StorageKey
from .strategy import FSMStrategy


class FSMMiddleware:
    def __init__(self, storage: BaseStorage, strategy: FSMStrategy) -> None:
        self.storage = storage
        self.strategy = strategy

    async def __call__(
        self,
        handler: Callable[[Any, dict[str, Any]], Awaitable[Any]],
        event: Any,
        data: dict[str, Any],
    ) -> Any:
        bot = data.get("bot")
        key = self.resolve_event_key(bot if isinstance(bot, Bot) else None, event)
        if key is None:
            return await handler(event, data)

        context = FSMContext(self.storage, key)
        data["state"] = context
        data["raw_state"] = await context.get_state()
        data["fsm_storage_key"] = key
        return await handler(event, data)

    def resolve_event_key(self, bot: Bot | None, event: Any) -> StorageKey | None:
        peer_id = self._get_int_attr(event, "peer_id")
        user_id = self._get_int_attr(event, "from_id")
        if user_id is None:
            user_id = self._get_int_attr(event, "user_id")

        if peer_id is None and user_id is None:
            return None

        bot_id = bot.group_id if bot is not None else None
        fallback_user_id = user_id if user_id is not None else peer_id

        if self.strategy is FSMStrategy.USER:
            return StorageKey(bot_id=bot_id, peer_id=None, user_id=fallback_user_id)
        if self.strategy is FSMStrategy.PEER:
            return StorageKey(bot_id=bot_id, peer_id=peer_id, user_id=None)
        return StorageKey(bot_id=bot_id, peer_id=peer_id, user_id=fallback_user_id)

    def _get_int_attr(self, event: Any, name: str) -> int | None:
        value = getattr(event, name, None)
        return value if isinstance(value, int) else None
