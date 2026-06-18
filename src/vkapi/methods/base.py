from __future__ import annotations

from collections.abc import Generator
from typing import TYPE_CHECKING, Any, ClassVar, Generic, TypeVar

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from vkapi.client.bot import Bot

T = TypeVar("T")


class RawMethod(BaseModel, Generic[T]):
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="allow")

    method: str
    params: dict[str, Any] = {}

    @property
    def __api_method__(self) -> str:
        return self.method

    def build_request(self) -> dict[str, Any]:
        return dict(self.params)


class VKMethod(BaseModel, Generic[T]):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        extra="allow",
        populate_by_name=True,
    )

    __api_method__: ClassVar[str]
    __returning__: ClassVar[type[Any]] = Any
    _bot: Bot | None = None

    def as_(self, bot: Bot) -> VKMethod[T]:
        self._bot = bot
        return self

    def build_request(self) -> dict[str, Any]:
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)

    async def emit(self, bot: Bot) -> T:
        return await bot(self)

    def __await__(self) -> Generator[Any, None, T]:
        if self._bot is None:
            raise RuntimeError("Method is not mounted to a Bot. Use `await bot(method)`.")
        return self.emit(self._bot).__await__()


MethodT = VKMethod[T] | RawMethod[T]
