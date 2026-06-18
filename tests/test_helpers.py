from __future__ import annotations

import json

from vkapi import Keyboard, KeyboardButtonColor


def test_keyboard_json() -> None:
    keyboard = (
        Keyboard(inline=True)
        .add_text("A", payload={"a": 1}, color=KeyboardButtonColor.PRIMARY)
        .row()
        .add_callback("B", payload={"b": 2})
    )

    data = json.loads(keyboard.as_json())

    assert data["inline"] is True
    assert data["buttons"][0][0]["color"] == "primary"
    assert data["buttons"][0][0]["action"]["payload"] == '{"a": 1}'
    assert data["buttons"][1][0]["action"]["type"] == "callback"
