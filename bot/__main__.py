import asyncio
import logging

from bot.handlers import user_handlers
from dispatcher import dp, bot

logging.basicConfig(level=logging.INFO)



async def main():
    user_handlers.register_handlers(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
