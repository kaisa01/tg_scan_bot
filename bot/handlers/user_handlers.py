from aiogram import types
from aiogram.filters import Command

def register_handlers(dp):
    @dp.message(Command("start"))
    async def cmd_start(message: types.Message):
        await message.answer("Hello!")


