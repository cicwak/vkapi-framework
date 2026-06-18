Introduction
============

``vkapi`` provides an asynchronous VK API client, bot polling, routers, filters,
middlewares, dependency injection, keyboard helpers, and upload helpers.

Quick start
-----------

.. code-block:: python

   from vkapi import Bot, Dispatcher, Router
   from vkapi.filters import Command
   from vkapi.types import Message

   bot = Bot("TOKEN", group_id=123)
   dp = Dispatcher()
   router = Router()


   @router.message(Command("start"))
   async def start(message: Message) -> None:
       await message.answer("Hello")


   dp.include_router(router)
   dp.run_polling(bot)
