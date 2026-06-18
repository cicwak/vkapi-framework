from __future__ import annotations

from collections.abc import Callable
from typing import Any

from .base import Filter


class Text(Filter):
    def __init__(
        self,
        text: str | None = None,
        *,
        contains: str | None = None,
        startswith: str | None = None,
        endswith: str | None = None,
        ignore_case: bool = True,
        predicate: Callable[[str], bool] | None = None,
    ) -> None:
        self.text = text
        self.contains = contains
        self.startswith = startswith
        self.endswith = endswith
        self.ignore_case = ignore_case
        self.predicate = predicate

    async def __call__(self, event: Any, **kwargs: Any) -> bool:
        value = getattr(event, "text", "") or ""
        probe = value.lower() if self.ignore_case else value

        def norm(item: str | None) -> str | None:
            return item.lower() if item is not None and self.ignore_case else item

        if self.text is not None and probe != norm(self.text):
            return False
        if self.contains is not None and norm(self.contains) not in probe:
            return False
        if self.startswith is not None and not probe.startswith(norm(self.startswith) or ""):
            return False
        if self.endswith is not None and not probe.endswith(norm(self.endswith) or ""):
            return False
        return not (self.predicate is not None and not self.predicate(value))
