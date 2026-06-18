# vkapi

Async-first SDK and bot framework for VK API inspired by aiogram 3.

## Installation

```bash
pip install vkapi-framework
```

The PyPI distribution is named `vkapi-framework`; the Python package is imported
as `vkapi`.

## Quick start

```python
from vkapi import Bot, Dispatcher, Router
from vkapi.filters import Command
from vkapi.types import Message

bot = Bot("TOKEN", group_id=123)
dp = Dispatcher()
router = Router()


@router.message(Command("start"))
async def start(message: Message) -> None:
    await message.answer("Привет")


dp.include_router(router)
dp.run_polling(bot)
```

The first implementation focuses on community Bots Long Poll, typed method objects,
raw VK API fallback, routers, filters, middlewares, dependency injection, keyboards,
and common upload flows.

## Requirements

- Python 3.11-3.14
- aiohttp 3.9+
- pydantic 2.4+

## Development

```bash
uv sync --extra dev
uv run pytest
uv run ruff check .
uv run mypy
```

## Build

```bash
uv build
uv run twine check dist/*
```

## License

MIT
