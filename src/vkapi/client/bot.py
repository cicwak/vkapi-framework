from __future__ import annotations

import random
from typing import Any, TypeVar, cast

from vkapi.client.session.aiohttp import AiohttpSession
from vkapi.client.session.base import BaseSession
from vkapi.exceptions import VKAPIResponseError, VKRateLimitError
from vkapi.methods.base import MethodT, RawMethod
from vkapi.rate_limit import AsyncRateLimiter

T = TypeVar("T")


class RawAPINamespace:
    def __init__(self, bot: Bot, name: str) -> None:
        self._bot = bot
        self._name = name

    def __getattr__(self, method_name: str) -> Any:
        async def caller(**params: Any) -> Any:
            return await self._bot.api(f"{self._name}.{method_name}", **params)

        return caller


class Bot:
    def __init__(
        self,
        token: str,
        *,
        group_id: int | None = None,
        api_version: str = "5.199",
        session: BaseSession | None = None,
        default: dict[str, Any] | None = None,
        rate_limit: float | None = None,
        retry_rate_limit: bool = False,
    ) -> None:
        self.token = token
        self.group_id = group_id
        self.api_version = api_version
        self.session = session or AiohttpSession()
        self.default = default or {}
        self.retry_rate_limit = retry_rate_limit
        if rate_limit is None:
            rate_limit = 20.0 if group_id is not None else 3.0
        self.rate_limiter = AsyncRateLimiter(rate_limit)
        self._namespaces: dict[str, Any] = {}
        self._install_generated_namespaces()
        from vkapi.upload import Upload

        self.upload = Upload(self)

    def _install_generated_namespaces(self) -> None:
        method_groups: dict[str, Any]
        try:
            from vkapi.methods.generated import METHOD_GROUPS as generated_method_groups

            method_groups = generated_method_groups
        except ImportError:
            method_groups = {}
        for group_name, namespace_cls in method_groups.items():
            if group_name == "api":
                continue
            namespace = namespace_cls(self)
            self._namespaces[group_name] = namespace
            setattr(self, group_name, namespace)

    def __getattr__(self, name: str) -> RawAPINamespace:
        if name.startswith("_"):
            raise AttributeError(name)
        namespace = RawAPINamespace(self, name)
        self._namespaces[name] = namespace
        setattr(self, name, namespace)
        return namespace

    async def __call__(
        self,
        method: MethodT[T],
        *,
        request_timeout: float | None = None,
    ) -> T:
        await self.rate_limiter.acquire()
        try:
            return await self.session(self, method, request_timeout)
        except VKRateLimitError:
            if not self.retry_rate_limit:
                raise
            await self.rate_limiter.acquire()
            return await self.session(self, method, request_timeout)

    async def api(self, method: str, **params: Any) -> Any:
        return await self(RawMethod(method=method, params=params))

    async def close(self) -> None:
        await self.session.close()

    async def get_long_poll_server(self) -> dict[str, Any]:
        if self.group_id is None:
            raise RuntimeError("Bot.group_id is required for Bots Long Poll")
        result = await self.api("groups.getLongPollServer", group_id=self.group_id)
        return cast(dict[str, Any], result)

    def next_random_id(self) -> int:
        return random.randint(-(2**31), 2**31 - 1)

    async def send_message(
        self,
        *,
        peer_id: int,
        message: str | None = None,
        random_id: int | None = None,
        **kwargs: Any,
    ) -> Any:
        if random_id is None:
            random_id = self.next_random_id()
        return await self.api(
            "messages.send",
            peer_id=peer_id,
            random_id=random_id,
            message=message,
            **kwargs,
        )

    async def delete_message(
        self,
        *,
        peer_id: int | None = None,
        cmids: list[int] | None = None,
    ) -> Any:
        params: dict[str, Any] = {}
        if peer_id is not None:
            params["peer_id"] = peer_id
        if cmids is not None:
            params["cmids"] = cmids
        return await self.api("messages.delete", **params)

    async def edit_message(
        self,
        *,
        peer_id: int,
        message: str | None = None,
        cmid: int | None = None,
        message_id: int | None = None,
        **kwargs: Any,
    ) -> Any:
        return await self.api(
            "messages.edit",
            peer_id=peer_id,
            message=message,
            cmid=cmid,
            message_id=message_id,
            **kwargs,
        )

    def raise_for_group(self) -> int:
        if self.group_id is None:
            raise VKAPIResponseError(error_code=0, error_msg="Bot.group_id is required")
        return self.group_id
