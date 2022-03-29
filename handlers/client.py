import buttons.user_kb
from aiogram import types, Dispatcher


async def start(message : types.Message):
    await message.reply('Hello again', reply_markup=buttons.user_kb.kb_client)

async def eho(message : types.Message):
    await message.answer(message.text,)


def register_handler_client(dp : Dispatcher):
    dp.register_message_handler(start, commands=['start', 'help'])
    dp.register_message_handler(eho)
