import asyncio

from aiogram import Bot, Dispatcher

from app.config import settings
from app.logging import configure_logging
from bot.handlers.start import router as start_router


async def run_bot() -> None:
    configure_logging()
    if not settings.telegram_bot_token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN is not configured")

    bot = Bot(token=settings.telegram_bot_token)
    dp = Dispatcher()
    dp.include_router(start_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(run_bot())
