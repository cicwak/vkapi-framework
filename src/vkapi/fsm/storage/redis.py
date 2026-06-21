from __future__ import annotations

import inspect
import json
from importlib import import_module
from typing import Any, cast

from .base import StorageKey


class RedisStorage:
    def __init__(
        self,
        redis: Any,
        *,
        key_prefix: str = "vkapi:fsm",
        state_ttl: int | None = None,
        data_ttl: int | None = None,
    ) -> None:
        self.redis = redis
        self.key_prefix = key_prefix
        self.state_ttl = state_ttl
        self.data_ttl = data_ttl

    @classmethod
    def from_url(cls, url: str, **kwargs: Any) -> RedisStorage:
        try:
            redis_module = import_module("redis.asyncio")
        except ImportError as exc:
            raise RuntimeError("Install vkapi-framework[redis] to use RedisStorage") from exc
        redis = redis_module.from_url(url, decode_responses=True, **kwargs)
        return cls(redis)

    async def get_state(self, key: StorageKey) -> str | None:
        value = await self.redis.get(self._state_key(key))
        return value if isinstance(value, str) else None

    async def set_state(self, key: StorageKey, state: str | None) -> None:
        redis_key = self._state_key(key)
        if state is None:
            await self.redis.delete(redis_key)
            return
        if self.state_ttl is None:
            await self.redis.set(redis_key, state)
        else:
            await self.redis.set(redis_key, state, ex=self.state_ttl)

    async def get_data(self, key: StorageKey) -> dict[str, Any]:
        value = await self.redis.get(self._data_key(key))
        if not isinstance(value, str):
            return {}
        data = json.loads(value)
        return cast(dict[str, Any], data if isinstance(data, dict) else {})

    async def set_data(self, key: StorageKey, data: dict[str, Any]) -> None:
        redis_key = self._data_key(key)
        if not data:
            await self.redis.delete(redis_key)
            return
        payload = json.dumps(data)
        if self.data_ttl is None:
            await self.redis.set(redis_key, payload)
        else:
            await self.redis.set(redis_key, payload, ex=self.data_ttl)

    async def close(self) -> None:
        close = getattr(self.redis, "aclose", None) or getattr(self.redis, "close", None)
        if close is None:
            return
        result = close()
        if inspect.isawaitable(result):
            await result

    def _state_key(self, key: StorageKey) -> str:
        return f"{self.key_prefix}:{key.as_string()}:state"

    def _data_key(self, key: StorageKey) -> str:
        return f"{self.key_prefix}:{key.as_string()}:data"
