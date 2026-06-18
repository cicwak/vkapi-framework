from __future__ import annotations

from collections.abc import Generator
from typing import Any

from .event.bases import UNHANDLED
from .event.observer import EventObserver

DEFAULT_EVENT_TYPES = (
    "message_new",
    "message_reply",
    "message_edit",
    "message_allow",
    "message_deny",
    "message_event",
    "wall_post_new",
    "wall_reply_new",
    "wall_reply_edit",
    "wall_reply_delete",
    "wall_reply_restore",
    "photo_new",
    "photo_comment_new",
    "video_new",
    "video_comment_new",
    "audio_new",
    "board_post_new",
    "update",
    "error",
)


class Router:
    def __init__(self, *, name: str | None = None) -> None:
        self.name = name or hex(id(self))
        self._parent_router: Router | None = None
        self.sub_routers: list[Router] = []
        self.observers: dict[str, EventObserver] = {
            event_type: EventObserver(self, event_type) for event_type in DEFAULT_EVENT_TYPES
        }
        self.message = self.observers["message_new"]
        self.message_reply = self.observers["message_reply"]
        self.message_edit = self.observers["message_edit"]
        self.message_allow = self.observers["message_allow"]
        self.message_deny = self.observers["message_deny"]
        self.message_event = self.observers["message_event"]
        self.update = self.observers["update"]
        self.errors = self.error = self.observers["error"]

    @property
    def parent_router(self) -> Router | None:
        return self._parent_router

    @parent_router.setter
    def parent_router(self, router: Router) -> None:
        if self._parent_router is not None:
            raise RuntimeError("Router is already attached")
        if router is self:
            raise RuntimeError("Self-referencing router is not allowed")
        parent: Router | None = router
        while parent is not None:
            if parent is self:
                raise RuntimeError("Circular router reference is not allowed")
            parent = parent.parent_router
        self._parent_router = router
        router.sub_routers.append(self)

    @property
    def chain_head(self) -> Generator[Router, None, None]:
        router: Router | None = self
        while router:
            yield router
            router = router.parent_router

    @property
    def chain_tail(self) -> Generator[Router, None, None]:
        yield self
        for router in self.sub_routers:
            yield from router.chain_tail

    def include_router(self, router: Router) -> Router:
        router.parent_router = self
        return router

    def include_routers(self, *routers: Router) -> None:
        for router in routers:
            self.include_router(router)

    def resolve_used_update_types(self) -> list[str]:
        used: set[str] = set()
        for router in self.chain_tail:
            for name, observer in router.observers.items():
                if observer.handlers and name not in {"update", "error"}:
                    used.add(name)
        return sorted(used)

    async def propagate_event(self, update_type: str, event: Any, **kwargs: Any) -> Any:
        observer = self.observers.get(update_type)

        async def wrapped(current_event: Any, data: dict[str, Any]) -> Any:
            return await self._propagate_event(observer, update_type, current_event, **data)

        if observer:
            return await observer.wrap_outer_middleware(wrapped, event, kwargs)
        return await wrapped(event, kwargs)

    async def _propagate_event(
        self,
        observer: EventObserver | None,
        update_type: str,
        event: Any,
        **kwargs: Any,
    ) -> Any:
        response = UNHANDLED
        if observer:
            result, data = await observer.check_root_filters(event, **kwargs)
            if not result:
                return UNHANDLED
            kwargs.update(data)
            response = await observer.trigger(event, **kwargs)
            if response is not UNHANDLED:
                return response
        for router in self.sub_routers:
            response = await router.propagate_event(update_type, event, **kwargs)
            if response is not UNHANDLED:
                return response
        return response
