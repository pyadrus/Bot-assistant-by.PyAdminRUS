import datetime
import os
import sqlite3

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loguru import logger

from keyboards.welcome_keyboard import keyboard_go_back
from system.system import dp, bot

logger.add('log/log.log')


@dp.callback_query_handler(lambda c: c.data in ['sample_orders'])
async def sample_orders(callback_query: types.CallbackQuery):
    """Кнопки с месяцами рапорта"""
    keyboard = InlineKeyboardMarkup()
    payment_on_public_holidays = InlineKeyboardButton(text=f'Оплата за праздничный день',
                                                      callback_data='payment_on_public_holidays')
    day_off_for_public_holiday = InlineKeyboardButton(text=f'Выходной за праздничный день',
                                                      callback_data='day_off_for_public_holiday')
    return_to_menu_button = InlineKeyboardButton(text='↩️  Вернуться в начальное меню', callback_data='menu')
    keyboard.row(payment_on_public_holidays)
    keyboard.row(day_off_for_public_holiday)
    keyboard.row(return_to_menu_button)
    await bot.send_message(callback_query.from_user.id, "Выберите приказ:", reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data in ['payment_on_public_holidays'])
async def payment_on_public_holidays(callback_query: types.CallbackQuery, state: FSMContext):
    """Образец приказа оплата в праздничные дни"""
    try:
        user_id = callback_query.from_user.id
        username = callback_query.from_user.username
        timestamp = datetime.datetime.now()
        file_name = 'Оплата праздничные дни.doc'
        perform_database_operations(user_id, username, timestamp, file_name)

        # Поиск и отправка файла
        file_path = "raports/sample_orders/Оплата праздничные дни.doc"
        if os.path.isfile(file_path):
            with open(file_path, "rb") as file:
                keyboard_return = keyboard_go_back()
                await bot.send_document(callback_query.from_user.id, document=file,
                                        caption=f"Образец приказа: {file_name}", reply_markup=keyboard_return)
    except Exception as e:
        logger.error(f"An error occurred: {e}")

    await state.finish()


@dp.callback_query_handler(lambda c: c.data in ['day_off_for_public_holiday'])
async def day_off_for_public_holiday(callback_query: types.CallbackQuery, state: FSMContext):
    """Образец приказа выходной за праздничный день"""
    try:
        user_id = callback_query.from_user.id
        username = callback_query.from_user.username
        timestamp = datetime.datetime.now()
        file_name = 'Выходной за отработанный праздничный день.doc'
        perform_database_operations(user_id, username, timestamp, file_name)

        # Поиск и отправка файла
        file_path = "raports/sample_orders/Выходной за отработанный праздничный день.doc"
        if os.path.isfile(file_path):
            with open(file_path, "rb") as file:
                keyboard_return = keyboard_go_back()
                await bot.send_document(callback_query.from_user.id, document=file,
                                        caption=f"Образец приказа: {file_name}", reply_markup=keyboard_return)
    except Exception as e:
        logger.error(f"An error occurred: {e}")

    await state.finish()


def perform_database_operations(user_id, username, timestamp, file_name):
    """Определение функции для операций с базой данных"""
    conn = sqlite3.connect('settings/database.db')
    cursor = conn.cursor()
    # Создайте таблицу, если она не существует
    cursor.execute("""CREATE TABLE IF NOT EXISTS user_requests (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER,
                                                                username TEXT, timestamp TEXT, file_name TEXT)""")
    # Вставка записи в таблицу
    cursor.execute("""INSERT INTO user_requests (user_id, username, timestamp, file_name) 
                      VALUES (?, ?, ?, ?)""", (user_id, username, timestamp, file_name))
    # Зафиксируйте изменения в базе данных
    conn.commit()
    conn.close()


def register_sample_orders_handler():
    """Регистрируем handlers для работы в выходной день"""
    dp.register_message_handler(sample_orders)
