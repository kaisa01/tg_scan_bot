import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from handlers import user_handlers  # Импортируем обработчики

logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="7674129807:AAEvVceoiyoQMxoaIJmwTbHLF_G3i1NL05E")
# Диспетчер
dp = Dispatcher()


async def main():
    user_handlers.register_handlers(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

