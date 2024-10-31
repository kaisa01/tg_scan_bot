from aiogram import types

def register_handlers(dp):
    @dp.message_handler(commands=['start', 'help'])
    async def cmd_test1(message: types.Message):
        await message.answer("Hello!")


    # Хэндлер на команду /test2
    async def cmd_test2(message: types.Message):
        await message.answer("Test 2")



