from __future__ import annotations

import json
from enum import StrEnum
from typing import Any

from pydantic import BaseModel, ConfigDict


def _payload_json(payload: dict[str, Any] | str) -> str:
    return json.dumps(payload, ensure_ascii=False) if isinstance(payload, dict) else payload


class KeyboardButtonColor(StrEnum):
    PRIMARY = "primary"
    SECONDARY = "secondary"
    NEGATIVE = "negative"
    POSITIVE = "positive"


class KeyboardButton(BaseModel):
    model_config = ConfigDict(extra="allow")

    action: dict[str, Any]
    color: KeyboardButtonColor | None = None


class Keyboard:
    def __init__(self, *, one_time: bool = False, inline: bool = False) -> None:
        self.one_time = one_time
        self.inline = inline
        self.buttons: list[list[KeyboardButton]] = [[]]

    def row(self) -> Keyboard:
        if self.buttons[-1]:
            self.buttons.append([])
        return self

    def add_text(
        self,
        label: str,
        *,
        payload: dict[str, Any] | str | None = None,
        color: KeyboardButtonColor = KeyboardButtonColor.SECONDARY,
    ) -> Keyboard:
        action: dict[str, Any] = {"type": "text", "label": label}
        if payload is not None:
            action["payload"] = _payload_json(payload)
        self.buttons[-1].append(KeyboardButton(action=action, color=color))
        return self

    def add_callback(
        self,
        label: str,
        *,
        payload: dict[str, Any] | str,
        color: KeyboardButtonColor = KeyboardButtonColor.SECONDARY,
    ) -> Keyboard:
        action: dict[str, Any] = {
            "type": "callback",
            "label": label,
            "payload": _payload_json(payload),
        }
        self.buttons[-1].append(KeyboardButton(action=action, color=color))
        return self

    def add_open_link(
        self,
        label: str,
        *,
        link: str,
        payload: dict[str, Any] | str | None = None,
    ) -> Keyboard:
        action: dict[str, Any] = {"type": "open_link", "label": label, "link": link}
        if payload is not None:
            action["payload"] = _payload_json(payload)
        self.buttons[-1].append(KeyboardButton(action=action))
        return self

    def as_dict(self) -> dict[str, Any]:
        rows = [
            [button.model_dump(mode="json", exclude_none=True) for button in row]
            for row in self.buttons
            if row
        ]
        return {"one_time": self.one_time, "inline": self.inline, "buttons": rows}

    def as_json(self) -> str:
        return json.dumps(self.as_dict(), ensure_ascii=False)

    def __str__(self) -> str:
        return self.as_json()
