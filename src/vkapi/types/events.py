from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

from pydantic import BaseModel, ConfigDict, Field, PrivateAttr

if TYPE_CHECKING:
    from vkapi.client.bot import Bot


class VKObject(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    _bot: Bot | None = PrivateAttr(default=None)
    _update: Update | None = PrivateAttr(default=None)

    @property
    def bot(self) -> Bot:
        if self._bot is None:
            raise RuntimeError("Object is not mounted to a Bot")
        return self._bot

    def as_(self, bot: Bot, update: Update | None = None) -> VKObject:
        self._bot = bot
        self._update = update
        return self


class Message(VKObject):
    id: int | None = None
    date: int | None = None
    peer_id: int
    from_id: int | None = None
    text: str = ""
    random_id: int | None = None
    conversation_message_id: int | None = None
    payload: str | dict[str, Any] | None = None
    attachments: list[Any] = Field(default_factory=list)
    action: dict[str, Any] | None = None

    @property
    def payload_data(self) -> Any:
        if isinstance(self.payload, str):
            try:
                return json.loads(self.payload)
            except ValueError:
                return self.payload
        return self.payload

    async def answer(self, message: str | None = None, **kwargs: Any) -> Any:
        return await self.bot.send_message(peer_id=self.peer_id, message=message, **kwargs)

    async def reply(self, message: str | None = None, **kwargs: Any) -> Any:
        if self.conversation_message_id is not None:
            kwargs.setdefault("reply_to", self.conversation_message_id)
        elif self.id is not None:
            kwargs.setdefault("reply_to", self.id)
        return await self.answer(message, **kwargs)

    async def edit(self, message: str | None = None, **kwargs: Any) -> Any:
        return await self.bot.edit_message(
            peer_id=self.peer_id,
            message=message,
            cmid=self.conversation_message_id,
            message_id=self.id,
            **kwargs,
        )

    async def delete(self) -> Any:
        cmids = (
            [self.conversation_message_id]
            if self.conversation_message_id is not None
            else None
        )
        return await self.bot.delete_message(peer_id=self.peer_id, cmids=cmids)


class MessageEvent(VKObject):
    peer_id: int
    user_id: int | None = None
    conversation_message_id: int | None = None
    event_id: str | None = None
    payload: dict[str, Any] | str | None = None

    async def answer(self, **kwargs: Any) -> Any:
        if self.event_id is None:
            raise RuntimeError("message_event has no event_id")
        return await self.bot.api(
            "messages.sendMessageEventAnswer",
            event_id=self.event_id,
            user_id=self.user_id,
            peer_id=self.peer_id,
            **kwargs,
        )


class Update(VKObject):
    type: str
    object: dict[str, Any] = Field(default_factory=dict)
    group_id: int | None = None
    event_id: str | None = None
    v: str | None = None

    @property
    def event_type(self) -> str:
        return self.type

    @property
    def event(self) -> VKObject:
        if self.type in {"message_new", "message_reply", "message_edit"}:
            payload = self.object.get("message", self.object)
            return Message.model_validate(payload).as_(self.bot, self)
        if self.type == "message_event":
            payload = {**self.object}
            if self.event_id and "event_id" not in payload:
                payload["event_id"] = self.event_id
            return MessageEvent.model_validate(payload).as_(self.bot, self)
        return VKObject.model_validate(self.object).as_(self.bot, self)
