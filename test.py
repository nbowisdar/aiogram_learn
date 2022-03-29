from aiogram import executor
import config
import logging
import handlers
from aiogram.contrib.fsm_storage.memory import  MemoryStorage

storage = MemoryStorage()
#storage.

async def on_startup(info):
    print('Start executing bot!')

handlers.admin.register_commands_admin(config.dp)
handlers.client.register_handler_client(config.dp)


executor.start_polling(config.dp, skip_updates=True, on_startup=on_startup)