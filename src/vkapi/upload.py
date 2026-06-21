from __future__ import annotations

from pathlib import Path
from typing import Any, cast

from aiohttp import ClientSession, FormData

from vkapi.client.bot import Bot


class Upload:
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    async def _post_file(self, upload_url: str, field: str, path: str | Path) -> dict[str, Any]:
        file_path = Path(path)
        form = FormData()
        form.add_field(field, file_path.read_bytes(), filename=file_path.name)
        async with (
            ClientSession() as session,
            session.post(upload_url, data=form) as response,
        ):
            response.raise_for_status()
            payload = await response.json()
        if not isinstance(payload, dict):
            raise RuntimeError("VK upload response must be an object")
        return cast(dict[str, Any], payload)

    async def message_photo(self, peer_id: int, path: str | Path) -> str:
        server = cast(
            dict[str, Any],
            await self.bot.api("photos.getMessagesUploadServer", peer_id=peer_id),
        )
        upload = await self._post_file(str(server["upload_url"]), "photo", path)
        saved = await self.bot.api(
            "photos.saveMessagesPhoto",
            photo=upload.get("photo"),
            server=upload.get("server"),
            hash=upload.get("hash"),
        )
        item = cast(dict[str, Any], saved[0] if isinstance(saved, list) else saved)
        return f"photo{item['owner_id']}_{item['id']}"

    async def doc(self, peer_id: int, path: str | Path, *, type: str = "doc") -> str:
        server = cast(
            dict[str, Any],
            await self.bot.api("docs.getMessagesUploadServer", peer_id=peer_id, type=type),
        )
        upload = await self._post_file(str(server["upload_url"]), "file", path)
        saved = cast(dict[str, Any], await self.bot.api("docs.save", file=upload.get("file")))
        item = saved.get(type) or saved.get("doc") or saved
        return f"doc{item['owner_id']}_{item['id']}"

    async def audio_message(self, peer_id: int, path: str | Path) -> str:
        return await self.doc(peer_id, path, type="audio_message")
