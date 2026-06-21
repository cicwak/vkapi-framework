from __future__ import annotations

import asyncio
from typing import Any

from .base import StorageKey


class MemoryStorage:
    def __init__(self) -> None:
        self._states: dict[StorageKey, str] = {}
        self._data: dict[StorageKey, dict[str, Any]] = {}
        self._lock = asyncio.Lock()

    async def get_state(self, key: StorageKey) -> str | None:
        async with self._lock:
            return self._states.get(key)

    async def set_state(self, key: StorageKey, state: str | None) -> None:
        async with self._lock:
            if state is None:
                self._states.pop(key, None)
            else:
                self._states[key] = state

    async def get_data(self, key: StorageKey) -> dict[str, Any]:
        async with self._lock:
            return dict(self._data.get(key, {}))

    async def set_data(self, key: StorageKey, data: dict[str, Any]) -> None:
        async with self._lock:
            if data:
                self._data[key] = dict(data)
            else:
                self._data.pop(key, None)

    async def close(self) -> None:
        pass
