import sqlite3

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from aiogram.types import InputFile
import os
import math

storage = MemoryStorage()
BOT_TOKEN = '6140987401:AAGvPst8Ot2QEOv0VExkYcicGWLoBXanbmg'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)


class Form(StatesGroup):
    month = State()
    district = State()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    """Обрабатываем команду /start"""
    main_keyboard = InlineKeyboardMarkup()
    raport_button = InlineKeyboardButton(text='🔨Рапорта 2023', callback_data='rap')
    days_off_button = InlineKeyboardButton(text='📅 Выходные дни 2023', callback_data='days_off')
    main_keyboard.row(raport_button, days_off_button)
    await message.reply("Выберите пункт:", reply_markup=main_keyboard)


@dp.callback_query_handler(lambda c: c.data in ['days_off'])
async def days_off_callback_month(callback_query: types.CallbackQuery):
    """Плановые и выходные дни в Мае 2023"""
    keyboard = InlineKeyboardMarkup()
    may_button = InlineKeyboardButton(text='📅 Май 2023', callback_data='may_days_off')
    june_button = InlineKeyboardButton(text='📅 Июнь 2023', callback_data='june_days_off')
    keyboard.row(may_button, june_button)

    await bot.send_message(callback_query.from_user.id, "📅 Выберите месяц:", reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data in ['may_days_off'])
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    selected_month = callback_query.data
    await state.update_data(month=selected_month)
    await Form.district.set()

    norm_working_days = 19
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)

    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в Мае 2023:</code><b> {norm_working_days}</b>\n"
                                  f"\n<code>📅 Выходные:</code><b> 6, 7, 8, 13, 14, 20, 21, 27, 28</b>\n"
                                  f"<code>📅 Праздничные:</code><b> 1, 9, 11</b>\n"
                                  f"\n<code>📅 Выходные поверхность:</code><b> 1, 6, 7, 8, 9, 10, 13, 14, 20, 21, 27, 28</b>\n"
                                  f"<code>📅 Выходные подземные:</code><b>1, 3, 7, 8, 9, 11, 14, 17, 21, 24, 28</b>\n"
                                  f"\n<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML")

    await state.finish()


@dp.callback_query_handler(lambda c: c.data in ['june_days_off'])
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    selected_month = callback_query.data
    await state.update_data(month=selected_month)
    await Form.district.set()

    norm_working_days = 20
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)

    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в Июне 2023:</code><b> {norm_working_days}</b>\n"
                                  f"\n<code>📅 Выходные:</code><b> 3, 5, 10, 11, 17, 18, 24, 25</b>\n"
                                  f"<code>📅 Праздничные:</code><b> 4, 12</b>\n"
                                  f"\n<code>📅 Выходные поверхность:</code><b> 3, 4, 5, 10, 11, 12, 17, 18, 24, 25</b>\n"
                                  f"<code>📅 Выходные подземные:</code><b>4, 5, 7, 11, 12, 14, 18, 21, 25, 28</b>\n"
                                  f"\n<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML")

    await state.finish()


@dp.callback_query_handler(lambda c: c.data in ['rap'])
async def process_callback_month(callback_query: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup()
    mar_button = InlineKeyboardButton(text='📅 Март 2023', callback_data='mar_rap')
    keyboard.row(mar_button)
    await bot.send_message(callback_query.from_user.id, "📅 Выберите месяц:", reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data in ['mar_rap'])
async def process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
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

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Создаем таблицу, если ее нет
    cursor.execute("""CREATE TABLE IF NOT EXISTS user_requests (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER,
                                                                username TEXT, timestamp TEXT, file_name TEXT)""")
    # Добавляем запись в таблицу
    cursor.execute("""INSERT INTO user_requests (user_id, username, timestamp, file_name) 
                      VALUES (?, ?, ?, ?)""", (user_id, username, timestamp, file_name))
    conn.commit()

    # Поиск и отправка файла
    file_path = f"Рапорта/03_{month}_2023/{district}.xls"
    if os.path.isfile(file_path):
        with open(file_path, "rb") as file:
            await message.answer_document(InputFile(file))
    else:
        await message.answer("Файл не найден. Проверьте правильность введенного кода. Нажмите /start еще раз, "
                             "что бы повторить запрос")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
