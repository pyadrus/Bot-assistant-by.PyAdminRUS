# -*- coding: utf-8 -*-

from aiogram import types, F
import openpyxl
from datetime import date
from keyboards.welcome_keyboard import keyboard_go_back
from system.system import dp, bot, router


def determining_the_birthday():
    """Определение именинника"""
    # 📅 Получаем текущую дату и форматируем её как ДД.ММ
    today = date.today()
    current_day_month = today.strftime("%d.%m")

    # 📁 Открываем Excel-файл и выбираем активный лист
    workbook = openpyxl.load_workbook("settings/Списочный_состав_20200101.xlsx")
    sheet = workbook.active

    # 🎉 Список для хранения сообщений о днях рождения
    birthday_messages = []

    # 🔍 Перебираем строки с 6 по 2800 (включительно), столбцы F (6) до L (12)
    for row in sheet.iter_rows(
            min_row=6,
            max_row=2800,
            min_col=6,
            max_col=12,
            values_only=True
    ):
        # 🗓️ Дата рождения находится в последней колонке диапазона (L — индекс 6)
        birthday_cell = row[6]
        # ⚠️ Пропускаем строку, если значение не является строкой
        if not isinstance(birthday_cell, str):
            continue
        # 📆 Берём первые 5 символов (формат ДД.ММ)
        day_month = birthday_cell[:5]
        # 🎂 Проверяем совпадение с текущей датой
        if day_month == current_day_month:
            # 👤 Имя сотрудника из столбца G (индекс 1 в текущей строке)
            employee_name = row[1]
            # 🧾 Проверяем, есть ли информация об увольнении (столбец I — индекс 3)
            dismissal_date = row[3]
            # 💬 Формируем сообщение
            if dismissal_date is None:
                birthday_messages.append(f"👤 Имя:: {employee_name}")
            else:
                birthday_messages.append(f"👤 Имя: {employee_name}\n⛔ Уволен(а): {dismissal_date}")

    # 📢 Выводим все найденные совпадения
    return birthday_messages


@router.callback_query(F.data == "birthday")
async def birthday_handlers(callback_query: types.CallbackQuery):
    """Именинники на предприятии"""

    birthday_messages = determining_the_birthday()

    if not birthday_messages:
        message_text = "❌ Сегодня нет дней рождений 😕"
    else:
        # Объединяем все сообщения в одну строку с переносами
        formatted_birthdays = "\n\n".join(birthday_messages)
        message_text = (
            f"🎈 Поздравляем с днём рождения!\n\n"
            f"Сегодня свой день рождения отмечают сотрудники предприятия — как ныне работающие, так и те, кто ранее был с нами.\n"
            f"Желаем всем крепкого здоровья, благополучия и новых профессиональных успехов! 🎊\n\n"
            f"{formatted_birthdays}\n"
        )

    await bot.send_message(
        callback_query.from_user.id,
        message_text,
        reply_markup=keyboard_go_back()
    )


def register_birthday_handlers():
    """Регистрируем handlers для 🎂 именинников"""
    dp.register_message_handler(birthday_handlers)
