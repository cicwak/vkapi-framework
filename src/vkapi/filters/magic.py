from __future__ import annotations

from collections.abc import Callable
from typing import Any

from .base import Filter


class MagicFilter(Filter):
    def __init__(self, getter: Callable[[Any], Any] | None = None) -> None:
        self.getter = getter or (lambda event: event)

    def _chain(self, step: Callable[[Any], Any]) -> MagicFilter:
        def getter(event: Any) -> Any:
            return step(self.getter(event))

        return MagicFilter(getter)

    def __getattr__(self, item: str) -> MagicFilter:
        return self._chain(lambda value: getattr(value, item, None))

    def __getitem__(self, item: str) -> MagicFilter:
        return self._chain(lambda value: value.get(item) if isinstance(value, dict) else None)

    async def __call__(self, event: Any, **kwargs: Any) -> bool:
        return bool(self.getter(event))

    def __eq__(self, other: Any) -> Filter:  # type: ignore[override]
        return CompareFilter(self, lambda value: value == other)

    def __ne__(self, other: Any) -> Filter:  # type: ignore[override]
        return CompareFilter(self, lambda value: value != other)

    def contains(self, item: Any) -> Filter:
        return CompareFilter(self, lambda value: value is not None and item in value)

    def startswith(self, item: str) -> Filter:
        return CompareFilter(self, lambda value: isinstance(value, str) and value.startswith(item))

    def endswith(self, item: str) -> Filter:
        return CompareFilter(self, lambda value: isinstance(value, str) and value.endswith(item))


class CompareFilter(Filter):
    def __init__(self, magic: MagicFilter, predicate: Callable[[Any], bool]) -> None:
        self.magic = magic
        self.predicate = predicate

    async def __call__(self, event: Any, **kwargs: Any) -> bool:
        return self.predicate(self.magic.getter(event))


F = MagicFilter()
