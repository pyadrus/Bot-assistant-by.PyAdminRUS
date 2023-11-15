import math

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from system.global_variables import *
from system.global_variables_2022 import *
from system.system import dp, bot


@dp.callback_query_handler(lambda c: c.data in ['days_off_22'])
async def days_off_callback_month(callback_query: types.CallbackQuery):
    """Плановые и выходные дни в 2022 году"""
    keyboard = InlineKeyboardMarkup()

    jan_button = InlineKeyboardButton(text=f'✅ {jan_22}', callback_data='jan_days_off_2022')
    feb_button = InlineKeyboardButton(text=f'✅ {feb_22}', callback_data='feb_days_off_2022')
    mar_button = InlineKeyboardButton(text=f'✅ {mar_22}', callback_data='mar_days_off_2022')
    apr_button = InlineKeyboardButton(text=f'✅ {apr_22}', callback_data='apr_days_off_2022')
    may_button = InlineKeyboardButton(text=f'✅ {may_22}', callback_data='may_days_off_2022')
    jun_button = InlineKeyboardButton(text=f'✅ {june_22}', callback_data='june_days_off_2022')
    jul_button = InlineKeyboardButton(text=f'✅ {jul_22}', callback_data='jul_days_off_2022')
    aug_button = InlineKeyboardButton(text=f'✅ {aug_22}', callback_data='aug_days_off_2022')
    sep_button = InlineKeyboardButton(text=f'✅ {sep_22}', callback_data='sep_days_off_2022')
    oct_button = InlineKeyboardButton(text=f'✅ {oct_22}', callback_data='oct_days_off_2022')
    nov_button = InlineKeyboardButton(text=f'✅ {nov_22}', callback_data='nov_days_off_2022')
    dec_button = InlineKeyboardButton(text=f'✅ {dec_22}', callback_data='dec_days_off_2022')
    # Рабочие дни в году
    working_days_per_year = InlineKeyboardButton(text=f'🔨 Количество рабочих дней в 2022 году',
                                                 callback_data='working_days_per_year_2022')

    keyboard.row(jan_button, feb_button, mar_button)
    keyboard.row(apr_button, may_button, jun_button)
    keyboard.row(jul_button, aug_button, sep_button)
    keyboard.row(oct_button, nov_button, dec_button)
    keyboard.row(working_days_per_year)
    await bot.send_message(callback_query.from_user.id, "📅 Выберите месяц:", reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data in ['working_days_per_year_2022'])
async def working_days_per_year_process_callback(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Январе 2022"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)
    await Form.district.set()
    jan_2022 = 19  # 01
    feb_2022 = 19  # 02
    mar_2022 = 21  # 03
    apr_2022 = 20  # 04
    may_2022 = 17  # 05
    jun_2022 = 20  # 06
    jul_2022 = 20  # 07
    aug_2022 = 23  # 08
    sep_2022 = 22  # 09
    oct_2022 = 21  # 10
    nov_2022 = 21  # 11
    dec_2022 = 22  # 12
    days_all = (jan_2022 + feb_2022 + mar_2022 + apr_2022 + may_2022 + jun_2022 +
                jul_2022 + aug_2022 + sep_2022 + oct_2022 + nov_2022 + dec_2022)
    # создаем кнопку
    feedback_button = InlineKeyboardButton(text='⁉️ Задать вопрос, напомнить, замечание', callback_data='feedback')
    # создаем разметку для кнопки
    markup = InlineKeyboardMarkup().add(feedback_button)
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f"<code>Количество рабочих дней в 2022 году</code>\n"
                                  f"\n<code>Январь: {jan_2022}</code>\n"
                                  f"<code>Февраль: {feb_2022}</code>\n"
                                  f"<code>Март: {mar_2022}</code>\n"
                                  f"<code>Апрель: {apr_2022}</code>\n"
                                  f"<code>Май: {may_2022}</code>\n"
                                  f"<code>Июнь: {jun_2022}</code>\n"
                                  f"<code>Июль: {jul_2022}</code>\n"
                                  f"<code>Август: {aug_2022}</code>\n"
                                  f"<code>Сентябрь: {sep_2022}</code>\n"
                                  f"<code>Октябрь: {oct_2022}</code>\n"
                                  f"<code>Ноябрь: {nov_2022}</code>\n"
                                  f"<code>Декабрь: {dec_2022}</code>\n"
                                  f"\n<code>Всего: {days_all}</code>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML", reply_markup=markup)
    await state.finish()


@dp.callback_query_handler(lambda c: c.data in ['jan_days_off_2022'])
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Январе 2022"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)
    await Form.district.set()

    norm_working_days = 19
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)

    # создаем кнопку
    feedback_button = InlineKeyboardButton(text='⁉️ Задать вопрос, напомнить, замечание', callback_data='feedback')
    # создаем разметку для кнопки
    markup = InlineKeyboardMarkup().add(feedback_button)
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {jan_22}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {jan_22}:</code><b> {norm_working_days * 8}</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML", reply_markup=markup)
    await state.finish()


@dp.callback_query_handler(lambda c: c.data in ['feb_days_off_2022'])
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Феврале 2022"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)
    await Form.district.set()

    norm_working_days = 19
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)
    # создаем кнопку
    feedback_button = InlineKeyboardButton(text='⁉️ Задать вопрос, напомнить, замечание', callback_data='feedback')
    # создаем разметку для кнопки
    markup = InlineKeyboardMarkup().add(feedback_button)
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {feb_22}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {feb_22}:</code><b> {norm_working_days * 8}</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML", reply_markup=markup)
    await state.finish()


@dp.callback_query_handler(lambda c: c.data in ['mar_days_off_2022'])
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Марте 2022"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)
    await Form.district.set()

    norm_working_days = 21
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)
    # создаем кнопку
    feedback_button = InlineKeyboardButton(text='⁉️ Задать вопрос, напомнить, замечание', callback_data='feedback')
    # создаем разметку для кнопки
    markup = InlineKeyboardMarkup().add(feedback_button)
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {mar_22}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {mar_22}:</code><b> {norm_working_days * 8}</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML", reply_markup=markup)
    await state.finish()


@dp.callback_query_handler(lambda c: c.data in ['apr_days_off_2022'])
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Апреле 2022"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)
    await Form.district.set()

    norm_working_days = 20
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)
    # создаем кнопку
    feedback_button = InlineKeyboardButton(text='⁉️ Задать вопрос, напомнить, замечание', callback_data='feedback')
    # создаем разметку для кнопки
    markup = InlineKeyboardMarkup().add(feedback_button)
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {apr_22}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {apr_22}:</code><b> {norm_working_days * 8}</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML", reply_markup=markup)
    await state.finish()


@dp.callback_query_handler(lambda c: c.data in ['may_days_off_2022'])
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Мае 2022"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)
    await Form.district.set()

    norm_working_days = 17
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)
    # создаем кнопку
    feedback_button = InlineKeyboardButton(text='⁉️ Задать вопрос, напомнить, замечание', callback_data='feedback')
    # создаем разметку для кнопки
    markup = InlineKeyboardMarkup().add(feedback_button)
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {may_22}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {may_22}:</code><b> {norm_working_days * 8}</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML", reply_markup=markup)
    await state.finish()


@dp.callback_query_handler(lambda c: c.data in ['june_days_off_2022'])
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Июне 2022"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)
    await Form.district.set()

    norm_working_days = 20
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)
    # создаем кнопку
    feedback_button = InlineKeyboardButton(text='⁉️ Задать вопрос, напомнить, замечание', callback_data='feedback')
    # создаем разметку для кнопки
    markup = InlineKeyboardMarkup().add(feedback_button)
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {june_22}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {june_22}:</code><b> {norm_working_days * 8}</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML", reply_markup=markup)
    await state.finish()


@dp.callback_query_handler(lambda c: c.data in ['jul_days_off_2022'])
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Июле 2022"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)
    await Form.district.set()

    norm_working_days = 20
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)
    # создаем кнопку
    feedback_button = InlineKeyboardButton(text='⁉️ Задать вопрос, напомнить, замечание', callback_data='feedback')
    # создаем разметку для кнопки
    markup = InlineKeyboardMarkup().add(feedback_button)
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {jul_22}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {jul_22}:</code><b> {norm_working_days * 8}</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML", reply_markup=markup)
    await state.finish()


@dp.callback_query_handler(lambda c: c.data in ['aug_days_off_2022'])
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Августе 2022"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)
    await Form.district.set()

    norm_working_days = 23
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)
    # создаем кнопку
    feedback_button = InlineKeyboardButton(text='⁉️ Задать вопрос, напомнить, замечание', callback_data='feedback')
    # создаем разметку для кнопки
    markup = InlineKeyboardMarkup().add(feedback_button)
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {aug_22}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {aug_22}:</code><b> {norm_working_days * 8}</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML", reply_markup=markup)
    await state.finish()


@dp.callback_query_handler(lambda c: c.data in ['sep_days_off_2022'])
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Сентябре 2022"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)
    await Form.district.set()

    norm_working_days = 22
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)
    # создаем кнопку
    feedback_button = InlineKeyboardButton(text='⁉️ Задать вопрос, напомнить, замечание', callback_data='feedback')
    # создаем разметку для кнопки
    markup = InlineKeyboardMarkup().add(feedback_button)
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {sep_22}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {sep_22}:</code><b> {norm_working_days * 8}</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML", reply_markup=markup)
    await state.finish()


@dp.callback_query_handler(lambda c: c.data in ['oct_days_off_2022'])
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Октябре 2022"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)
    await Form.district.set()

    norm_working_days = 21
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)
    # создаем кнопку
    feedback_button = InlineKeyboardButton(text='⁉️ Задать вопрос, напомнить, замечание', callback_data='feedback')
    # создаем разметку для кнопки
    markup = InlineKeyboardMarkup().add(feedback_button)
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {oct_22}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {oct_22}:</code><b> {norm_working_days * 8}</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML", reply_markup=markup)
    await state.finish()


@dp.callback_query_handler(lambda c: c.data in ['nov_days_off_2022'])
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Ноябре 2022"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)
    await Form.district.set()

    norm_working_days = 21
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)
    # создаем кнопку
    feedback_button = InlineKeyboardButton(text='⁉️ Задать вопрос, напомнить, замечание', callback_data='feedback')
    # создаем разметку для кнопки
    markup = InlineKeyboardMarkup().add(feedback_button)
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {nov_22}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {nov_22}:</code><b> {norm_working_days * 8}</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML", reply_markup=markup)
    await state.finish()


@dp.callback_query_handler(lambda c: c.data in ['dec_days_off_2022'])
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Декабре 2022"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)
    await Form.district.set()

    norm_working_days = 22
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)
    # создаем кнопку
    feedback_button = InlineKeyboardButton(text='⁉️ Задать вопрос, напомнить, замечание', callback_data='feedback')
    # создаем разметку для кнопки
    markup = InlineKeyboardMarkup().add(feedback_button)
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {dec_22}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {dec_22}:</code><b> {norm_working_days * 8}</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML", reply_markup=markup)
    await state.finish()


def day_off_handler_22():
    """Регистрируем handlers для работы в выходной день"""
    dp.register_message_handler(days_off_callback_month)
