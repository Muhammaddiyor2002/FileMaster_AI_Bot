from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.keyboards.main_menu import main_menu_keyboard

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(
        "Assalomu alaykum! FileMaster AI Bot'ga xush kelibsiz. Faylingizni yuboring.",
        reply_markup=main_menu_keyboard(),
    )
