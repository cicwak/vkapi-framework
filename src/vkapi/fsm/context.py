from __future__ import annotations

from typing import Any

from .state import State, state_to_str
from .storage.base import BaseStorage, StorageKey


class FSMContext:
    def __init__(self, storage: BaseStorage, key: StorageKey) -> None:
        self.storage = storage
        self.key = key

    async def get_state(self) -> str | None:
        return await self.storage.get_state(self.key)

    async def set_state(self, state: State | str | None) -> None:
        await self.storage.set_state(self.key, state_to_str(state))

    async def clear(self) -> None:
        await self.storage.set_state(self.key, None)
        await self.storage.set_data(self.key, {})

    async def get_data(self) -> dict[str, Any]:
        return await self.storage.get_data(self.key)

    async def set_data(self, data: dict[str, Any]) -> None:
        await self.storage.set_data(self.key, data)

    async def update_data(self, **kwargs: Any) -> dict[str, Any]:
        data = await self.get_data()
        data.update(kwargs)
        await self.set_data(data)
        return data
