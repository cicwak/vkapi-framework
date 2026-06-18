from __future__ import annotations

from collections.abc import Callable
from typing import Any

from vkapi.dispatcher.middlewares.base import MiddlewareManager

from .bases import UNHANDLED, SkipHandler
from .handler import CallbackType, HandlerObject


class EventObserver:
    def __init__(self, router: Any, event_name: str) -> None:
        self.router = router
        self.event_name = event_name
        self.handlers: list[HandlerObject] = []
        self.middleware = MiddlewareManager()
        self.outer_middleware = MiddlewareManager()
        self._root_filters: list[CallbackType] = []

    def filter(self, *filters: CallbackType) -> None:
        self._root_filters.extend(filters)

    def register(
        self,
        callback: CallbackType,
        *filters: CallbackType,
        flags: dict[str, Any] | None = None,
    ) -> CallbackType:
        self.handlers.append(HandlerObject(callback, list(filters), flags or {}))
        return callback

    def __call__(
        self,
        *filters: CallbackType,
        flags: dict[str, Any] | None = None,
    ) -> Callable[[CallbackType], CallbackType]:
        def wrapper(callback: CallbackType) -> CallbackType:
            return self.register(callback, *filters, flags=flags)

        return wrapper

    async def check_root_filters(self, event: Any, **kwargs: Any) -> tuple[bool, dict[str, Any]]:
        handler = HandlerObject(lambda: True, list(self._root_filters))
        return await handler.check(event, **kwargs)

    def _resolve_middlewares(self) -> list[Any]:
        middlewares: list[Any] = []
        for router in reversed(tuple(self.router.chain_head)):
            observer = router.observers.get(self.event_name)
            if observer:
                middlewares.extend(observer.middleware)
        return middlewares

    def wrap_outer_middleware(self, callback: Any, event: Any, data: dict[str, Any]) -> Any:
        wrapped = self.middleware.wrap(list(self.outer_middleware), callback)
        return wrapped(event, data)

    async def trigger(self, event: Any, **kwargs: Any) -> Any:
        for handler in self.handlers:
            kwargs["handler"] = handler
            result, data = await handler.check(event, **kwargs)
            if result:
                kwargs.update(data)
                try:
                    wrapped = self.middleware.wrap(self._resolve_middlewares(), handler.call)
                    return await wrapped(event, kwargs)
                except SkipHandler:
                    continue
        return UNHANDLED
