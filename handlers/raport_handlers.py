import os
import sqlite3

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import InputFile

from system.global_variables import *
from system.system import dp, bot


@dp.callback_query_handler(lambda c: c.data in ['rap'])
async def process_callback_month(callback_query: types.CallbackQuery):
    """Кнопки с месяцами рапорта"""
    keyboard = InlineKeyboardMarkup()
    jan_button = InlineKeyboardButton(text=f'✅ {jan}', callback_data='01_jan_rap')
    feb_button = InlineKeyboardButton(text=f'✅ {feb}', callback_data='02_feb_rap')
    mar_button = InlineKeyboardButton(text=f'✅ {mar}', callback_data='03_mar_rap')
    apr_button = InlineKeyboardButton(text=f'✅ {apr}', callback_data='04_apr_rap')
    may_button = InlineKeyboardButton(text=f'✅ {may}', callback_data='05_may_rap')
    jun_button = InlineKeyboardButton(text=f'✅ {june}', callback_data='06_jun_rap')
    jul_button = InlineKeyboardButton(text=f'✅ {jul}', callback_data='07_jul_rap')
    aug_button = InlineKeyboardButton(text=f'✅ {aug}', callback_data='08_aug_rap')
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


list_of_plots_2023 = {110100: "Руководство", 110110: "Тех.служба", 110120: "Производ.служба", 110130: "Техн.служба",
                      110140: "СОТ и ТБ", 110150: "Маркшейдерская служба", 110160: "Геологическая служба",
                      110170: "ЭМС", 110191: "ПЭО", 110192: "ООТиЗП", 110193: "Финансовый сектор",
                      110200: "Бухгалтерия", 110211: "Сектор договорной работы", 110220: "Сектор МТС", 110230: "ОК",
                      110240: "Сектор по социальным вопросам", 110250: "Юридический сектор", 120110: "Уч.№ 1",
                      120210: "УПР № 1", 120220: "УПР № 2", 120400: "Уч.ШТ", 120410: "УКТ № 1", 120420: "УКТ № 2",
                      120500: "Уч.РВР", 120520: "Уч.РВР №2", 120610: "Уч.МДГО № 1", 120700: "ВТБ", 120800: "Уч.ВР",
                      120900: "ПРТБ", 121000: "Водоотлив", 121010: "Стац.оборуд.№1", 121020: "Стац.оборуд №2",
                      121030: "Электроцех", 121040: "РЗО", 121050: "ОМК", 121060: "РВВ", 121070: "Котельная",
                      121100: "Отдел технич-го контроля угля", 121110: "Участок АСУиТП", 121200: "Связь",
                      121400: "АБК", 121500: "Здравпункт", 121600: "Охрана", 121710: "Автотранспортный участок",
                      121730: "УФПО", 121800: "ОФ", 121810: "ИТР ОФ", 121820: "ОП ОФ", 121830: "Электроцех ОФ",
                      121840: "Монтажно-демонтажная группа ОФ", 121850: "Ремонтная группа ОФ",
                      121860: "Углехимическая лаборатория ОФ", 121870: "АБК ОФ", 121900: "Служба складского хозяйства",
                      121940: "Склад №2", 121950: "Склад №3", 121960: "Склад строительных материалов",
                      121972: "Склад №4", 121970: "Угольный склад", 121971: "Лесной склад", 122100: "КГЭС",
                      122200: "Уч.по изг и рем.", 122400: "УСМР", 130010: "Общежитие №1", 130020: "Гостиница 'Олимп'",
                      130030: "ПТК 'Донецкий'"}

report_no_text_found = ("🚫 <b>Файл не найден или рапорт не сформирован.</b>\n"
                        "Проверьте правильность введенного кода участка.\n\n"
                        "Нажмите <b>'↩️  Вернуться в начальное меню'</b>, чтобы повторить запрос.")


@dp.message_handler(state=Form.district)
async def process_district(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        month = data['month']
        district = message.text
        try:
            district_name = list_of_plots_2023[int(district)]
            print(district_name)
            # Запись в базу данных
            user_id = message.from_user.id
            username = message.from_user.username
            timestamp = str(message.date)
            file_name = district + '.xls'
            perform_database_operations(user_id, username, timestamp, file_name)
            # Поиск и отправка файла
            file_path = f"raports/rap_2023/{month}_2023/{district}.xls"
            if os.path.isfile(file_path):
                with open(file_path, "rb") as file:
                    await message.answer_document(InputFile(file), caption=f"Рапорт участка: {district_name}")
            else:
                # Создаем клавиатуру с одной кнопкой "Отправить сообщение"
                keyboard = create_feedback_and_return_to_menu_keyboard()
                await message.answer(report_no_text_found, reply_markup=keyboard)
        except KeyError:
            # Создаем клавиатуру с одной кнопкой "Отправить сообщение"
            keyboard = create_feedback_and_return_to_menu_keyboard()
            await message.answer(report_no_text_found, reply_markup=keyboard)
        await state.finish()


# Определение функции для операций с базой данных
def perform_database_operations(user_id, username, timestamp, file_name):
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


def create_feedback_and_return_to_menu_keyboard():
    # Создаем клавиатуру с двумя кнопками
    keyboard = InlineKeyboardMarkup()
    feedback_button = InlineKeyboardButton(text='⁉️ Если рапорт не найден, нажмите ТУТ', callback_data='feedback')
    return_to_menu_button = InlineKeyboardButton(text='↩️  Вернуться в начальное меню', callback_data='menu')
    # Добавляем кнопки к клавиатуре
    keyboard.add(feedback_button)
    keyboard.add(return_to_menu_button)
    return keyboard
