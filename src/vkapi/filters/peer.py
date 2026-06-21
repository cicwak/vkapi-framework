from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, cast

from .base import Filter

PeerKind = Literal["user", "chat", "group", "email"]


class PeerType(Filter):
    def __init__(self, *peer_types: PeerKind) -> None:
        self.peer_types = set(peer_types)

    async def __call__(self, event: Any, **kwargs: Any) -> bool:
        peer_id = getattr(event, "peer_id", None)
        if peer_id is None:
            return False
        if peer_id >= 2_000_000_000:
            peer_type = "chat"
        elif peer_id < 0:
            peer_type = "group"
        elif peer_id > 0:
            peer_type = "user"
        else:
            peer_type = "email"
        return peer_type in self.peer_types


class ChatAction(Filter):
    def __init__(self, *types: str) -> None:
        self.types = set(types)

    async def __call__(self, event: Any, **kwargs: Any) -> bool:
        action = getattr(event, "action", None)
        if not isinstance(action, Mapping):
            return False
        action = cast(Mapping[str, Any], action)
        return action.get("type") in self.types
