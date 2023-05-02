import os
import sqlite3

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import InputFile

# from main import Form
from system.global_variables import *
from system.system import dp, bot


@dp.callback_query_handler(lambda c: c.data in ['rap'])
async def process_callback_month(callback_query: types.CallbackQuery):
    """Кнопки с месяцами рапорта"""
    keyboard = InlineKeyboardMarkup()
    jan_button = InlineKeyboardButton(text=f'✅ {jan}', callback_data='01_jan_rap')
    feb_button = InlineKeyboardButton(text=f'✅ {feb}', callback_data='02_feb_rap')
    mar_button = InlineKeyboardButton(text=f'✅ {mar}', callback_data='03_mar_rap')
    apr_button = InlineKeyboardButton(text=f'{apr}', callback_data='04_apr_rap')
    may_button = InlineKeyboardButton(text=f'{may}', callback_data='05_may_rap')
    jun_button = InlineKeyboardButton(text=f'{june}', callback_data='06_jun_rap')
    jul_button = InlineKeyboardButton(text=f'{jul}', callback_data='07_jul_rap')
    aug_button = InlineKeyboardButton(text=f'{aug}', callback_data='08_aug_rap')
    sep_button = InlineKeyboardButton(text=f'{sep}', callback_data='09_sep_rap')
    oct_button = InlineKeyboardButton(text=f'{oct}', callback_data='10_oct_rap')
    nov_button = InlineKeyboardButton(text=f'{nov}', callback_data='11_nov_rap')
    dec_button = InlineKeyboardButton(text=f'{dec}', callback_data='12_dec_rap')
    keyboard.row(jan_button, feb_button, mar_button)
    keyboard.row(apr_button, may_button, jun_button)
    keyboard.row(jul_button, aug_button, sep_button)
    keyboard.row(oct_button, nov_button, dec_button)
    await bot.send_message(callback_query.from_user.id, "📅 Выберите месяц:", reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data in ['01_jan_rap'])
async def process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Рапорта Март 2023"""
    month = callback_query.data
    await state.update_data(month=month)
    await Form.district.set()
    await bot.send_message(callback_query.from_user.id, "Введите код участка:")


@dp.callback_query_handler(lambda c: c.data in ['02_feb_rap'])
async def process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Рапорта Март 2023"""
    month = callback_query.data
    await state.update_data(month=month)
    await Form.district.set()
    await bot.send_message(callback_query.from_user.id, "Введите код участка:")


@dp.callback_query_handler(lambda c: c.data in ['03_mar_rap'])
async def process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Рапорта Март 2023"""
    month = callback_query.data
    await state.update_data(month=month)
    await Form.district.set()
    await bot.send_message(callback_query.from_user.id, "Введите код участка:")


@dp.callback_query_handler(lambda c: c.data in ['04_apr_rap'])
async def process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Рапорта Март 2023"""
    month = callback_query.data
    await state.update_data(month=month)
    await Form.district.set()
    await bot.send_message(callback_query.from_user.id, "Введите код участка:")


@dp.callback_query_handler(lambda c: c.data in ['05_may_rap'])
async def process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Рапорта Март 2023"""
    month = callback_query.data
    await state.update_data(month=month)
    await Form.district.set()
    await bot.send_message(callback_query.from_user.id, "Введите код участка:")


@dp.callback_query_handler(lambda c: c.data in ['06_jun_rap'])
async def process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Рапорта Март 2023"""
    month = callback_query.data
    await state.update_data(month=month)
    await Form.district.set()
    await bot.send_message(callback_query.from_user.id, "Введите код участка:")


@dp.callback_query_handler(lambda c: c.data in ['07_jul_rap'])
async def process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Рапорта Март 2023"""
    month = callback_query.data
    await state.update_data(month=month)
    await Form.district.set()
    await bot.send_message(callback_query.from_user.id, "Введите код участка:")


@dp.callback_query_handler(lambda c: c.data in ['08_aug_rap'])
async def process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Рапорта Март 2023"""
    month = callback_query.data
    await state.update_data(month=month)
    await Form.district.set()
    await bot.send_message(callback_query.from_user.id, "Введите код участка:")


@dp.callback_query_handler(lambda c: c.data in ['09_sep_rap'])
async def process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Рапорта Март 2023"""
    month = callback_query.data
    await state.update_data(month=month)
    await Form.district.set()
    await bot.send_message(callback_query.from_user.id, "Введите код участка:")


@dp.callback_query_handler(lambda c: c.data in ['10_oct_rap'])
async def process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Рапорта Март 2023"""
    month = callback_query.data
    await state.update_data(month=month)
    await Form.district.set()
    await bot.send_message(callback_query.from_user.id, "Введите код участка:")


@dp.callback_query_handler(lambda c: c.data in ['11_nov_rap'])
async def process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Рапорта Март 2023"""
    month = callback_query.data
    await state.update_data(month=month)
    await Form.district.set()
    await bot.send_message(callback_query.from_user.id, "Введите код участка:")


@dp.callback_query_handler(lambda c: c.data in ['12_dec_rap'])
async def process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Рапорта Март 2023"""
    month = callback_query.data
    await state.update_data(month=month)
    await Form.district.set()
    await bot.send_message(callback_query.from_user.id, "Введите код участка:")


@dp.message_handler(state=Form.district)
async def process_district(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        month = data['month']
        district = message.text

    # Запись в базу данных
    user_id = message.from_user.id
    username = message.from_user.username
    timestamp = str(message.date)
    file_name = district + '.xls'

    conn = sqlite3.connect('settings/database.db')
    cursor = conn.cursor()
    # Создаем таблицу, если ее нет
    cursor.execute("""CREATE TABLE IF NOT EXISTS user_requests (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER,
                                                                username TEXT, timestamp TEXT, file_name TEXT)""")
    # Добавляем запись в таблицу
    cursor.execute("""INSERT INTO user_requests (user_id, username, timestamp, file_name) 
                      VALUES (?, ?, ?, ?)""", (user_id, username, timestamp, file_name))
    conn.commit()

    # Поиск и отправка файла
    file_path = f"raports/{month}_2023/{district}.xls"
    if os.path.isfile(file_path):
        with open(file_path, "rb") as file:
            await message.answer_document(InputFile(file))
    else:
        await message.answer("Файл не найден. Проверьте правильность введенного кода. Нажмите /start еще раз, "
                             "что бы повторить запрос")
    await state.finish()
