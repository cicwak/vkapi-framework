from __future__ import annotations

from typing import Any

from .base import Filter


class Payload(Filter):
    def __init__(self, value: Any = None, **contains: Any) -> None:
        self.value = value
        self.contains = contains

    async def __call__(self, event: Any, **kwargs: Any) -> bool:
        payload = getattr(event, "payload_data", getattr(event, "payload", None))
        if self.value is not None and payload != self.value:
            return False
        if self.contains:
            if not isinstance(payload, dict):
                return False
            for key, value in self.contains.items():
                if payload.get(key) != value:
                    return False
        return True
