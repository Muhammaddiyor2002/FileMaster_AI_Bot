from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔄 Convert", callback_data="action:convert")],
            [InlineKeyboardButton(text="🗜 Compress", callback_data="action:compress")],
            [InlineKeyboardButton(text="📄 PDF Tools", callback_data="action:pdf")],
            [InlineKeyboardButton(text="🤖 AI Tools", callback_data="action:ai")],
        ]
    )
