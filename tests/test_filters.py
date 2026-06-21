from __future__ import annotations

from types import MappingProxyType, SimpleNamespace

import pytest

from vkapi.filters import ChatAction, F, Payload


@pytest.mark.asyncio
async def test_magic_filter_reads_mapping_values() -> None:
    matches = F["action"] == "go"
    misses = F["action"] == "stop"
    payload = MappingProxyType({"action": "go"})

    assert await matches(payload) is True
    assert await misses(payload) is False


@pytest.mark.asyncio
async def test_magic_filter_reads_attributes() -> None:
    matches = F.text.startswith("hello")
    event = SimpleNamespace(text="hello world")

    assert await matches(event) is True


@pytest.mark.asyncio
async def test_payload_filter_accepts_mapping_payload_data() -> None:
    event = SimpleNamespace(payload_data=MappingProxyType({"action": "go"}))

    assert await Payload(action="go")(event) is True
    assert await Payload(action="stop")(event) is False


@pytest.mark.asyncio
async def test_payload_filter_rejects_non_mapping_payload_data_for_contains() -> None:
    event = SimpleNamespace(payload_data="not-json")

    assert await Payload(action="go")(event) is False


@pytest.mark.asyncio
async def test_chat_action_accepts_mapping_action() -> None:
    event = SimpleNamespace(action=MappingProxyType({"type": "chat_invite_user"}))

    assert await ChatAction("chat_invite_user")(event) is True
    assert await ChatAction("chat_kick_user")(event) is False
