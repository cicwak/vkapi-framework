Introduction
============

``vkapi`` provides an asynchronous VK API client, bot polling, routers, filters,
middlewares, dependency injection, keyboard helpers, and upload helpers.

Installation
------------

.. code-block:: bash

   pip install vkapi-framework

The PyPI distribution is named ``vkapi-framework``. The Python package is
imported as ``vkapi``.

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

Calling VK methods
------------------

Generated VK API methods are available through namespaces on ``Bot``:

.. code-block:: python

   await bot.messages.send(
       peer_id=2_000_000_001,
       random_id=bot.next_random_id(),
       message="Hello",
   )

The same request can be represented as a method object:

.. code-block:: python

   from vkapi.methods import MessagesSend

   method = MessagesSend(peer_id=2_000_000_001, random_id=0, message="Hello")
   await bot(method)

For methods that are not yet generated, use the raw API helper:

.. code-block:: python

   await bot.api("messages.send", peer_id=2_000_000_001, random_id=0, message="Hello")

See :doc:`methods` for the full generated method list, VK documentation links,
required parameters, and more examples.

Upload helpers
--------------

``bot.upload`` wraps common multi-step upload flows and returns ready-to-send
attachment strings.

.. code-block:: python

   attachment = await bot.upload.message_photo(
       peer_id=2_000_000_001,
       path="/path/to/photo.jpg",
   )

   await bot.messages.send(
       peer_id=2_000_000_001,
       random_id=bot.next_random_id(),
       attachment=attachment,
   )
