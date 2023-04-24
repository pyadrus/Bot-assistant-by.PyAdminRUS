import sqlite3

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from aiogram.types import InputFile
import os

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
    raport_button = InlineKeyboardButton(text='Рапорта 2023', callback_data='rap')
    main_keyboard.row(raport_button)
    await message.reply("Выберите пункт:", reply_markup=main_keyboard)


@dp.callback_query_handler(lambda c: c.data in ['rap'])
async def process_callback_month(callback_query: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup()
    mar_button = InlineKeyboardButton(text='Март', callback_data='mar')
    keyboard.row(mar_button)
    await bot.send_message(callback_query.from_user.id, "Выберите месяц:", reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data in ['mar'])
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
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_requests (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER,
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
