from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from system.system import dp, bot


@dp.callback_query_handler(lambda c: c.data in ['table'])
async def table_handler(callback_query: types.CallbackQuery):
    """Плановые и выходные дни в 2022 году"""
    keyboard = InlineKeyboardMarkup()

    year_21 = InlineKeyboardButton(text=f'2021', callback_data='year_21')
    year_22 = InlineKeyboardButton(text=f'2022', callback_data='year_22')
    year_23 = InlineKeyboardButton(text=f'2023', callback_data='year_23')
    year_24 = InlineKeyboardButton(text=f'2024', callback_data='year_24')
    return_to_menu_button = InlineKeyboardButton(text='↩️  Вернуться в начальное меню', callback_data='menu')

    keyboard.row(year_21, year_22, year_23, year_24)
    keyboard.row(return_to_menu_button)
    await bot.send_message(callback_query.from_user.id, "📅 Выберите год:", reply_markup=keyboard)


def register_table_handler_handler():
    """Регистрируем handlers для работы в выходной день"""
    dp.register_message_handler(table_handler)
