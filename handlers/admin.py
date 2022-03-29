from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from config import dp
from aiogram.dispatcher.filters import Text

class FSMCAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

#@dp.message_handler(commands=['/register_new_god', '/reg'])
async def register_new_god(message : types.Message):
    await FSMCAdmin.photo.set()
    await message.reply('Give me the photo first')

#@dp.message_handler(content_types=['photo'], state=FSMCAdmin.photo)
async def get_photo(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id

#@dp.message_handler(commands=['/check'])
async def check_info(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        await message.reply('Hello, in my dictionary I have next'
                            'information')
        await message.answer(data)
    await state.finish()

async def t(message : types.Message):
    await message.reply('Hello')



def register_commands_admin(dp : Dispatcher):
    dp.register_message_handler(t, commands=['hello'])
    dp.register_message_handler(register_new_god, commands=['register_new_god', 'reg', 'upload_photo'])
    dp.register_message_handler(get_photo, content_types=['photo'], state=FSMCAdmin.photo)
    dp.register_message_handler(check_info, commands=['check'])



