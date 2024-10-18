from aiogram import types, F

from keyboards.welcome_keyboard import output_sheet_by_area
from system.system import dp, bot, router


@router.callback_query(F.data == "table")
async def table_handler(callback_query: types.CallbackQuery):
    """Плановые и выходные дни в 2022 году"""

    await bot.send_message(callback_query.from_user.id, "📅 Выберите год:", reply_markup=output_sheet_by_area())


def register_table_handler_handler():
    """Регистрируем handlers для работы в выходной день"""
    dp.register_message_handler(table_handler)
