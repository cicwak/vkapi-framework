from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol


@dataclass(frozen=True, slots=True)
class StorageKey:
    bot_id: int | None
    peer_id: int | None
    user_id: int | None

    def as_string(self) -> str:
        bot = self._part(self.bot_id)
        peer = self._part(self.peer_id)
        user = self._part(self.user_id)
        return f"bot:{bot}:peer:{peer}:user:{user}"

    def _part(self, value: int | None) -> str:
        return str(value) if value is not None else "none"


class BaseStorage(Protocol):
    async def get_state(self, key: StorageKey) -> str | None: ...

    async def set_state(self, key: StorageKey, state: str | None) -> None: ...

    async def get_data(self, key: StorageKey) -> dict[str, Any]: ...

    async def set_data(self, key: StorageKey, data: dict[str, Any]) -> None: ...

    async def close(self) -> None: ...
