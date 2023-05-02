import math

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# from main import Form
from system.global_variables import *
from system.system import dp, bot


@dp.callback_query_handler(lambda c: c.data in ['days_off'])
async def days_off_callback_month(callback_query: types.CallbackQuery):
    """Плановые и выходные дни в Мае 2023"""
    keyboard = InlineKeyboardMarkup()

    jan_button = InlineKeyboardButton(text=f'✅ {jan}', callback_data='jan_days_off')
    feb_button = InlineKeyboardButton(text=f'✅ {feb}', callback_data='feb_days_off')
    mar_button = InlineKeyboardButton(text=f'✅ {mar}', callback_data='mar_days_off')
    apr_button = InlineKeyboardButton(text=f'✅ {apr}', callback_data='apr_days_off')
    may_button = InlineKeyboardButton(text=f'✅ {may}', callback_data='may_days_off')
    june_button = InlineKeyboardButton(text=f'{june}', callback_data='june_days_off')
    jul_button = InlineKeyboardButton(text=f'{jul}', callback_data='jul_days_off')
    aug_button = InlineKeyboardButton(text=f'{aug}', callback_data='aug_days_off')
    sep_button = InlineKeyboardButton(text=f'{sep}', callback_data='sep_days_off')
    oct_button = InlineKeyboardButton(text=f'{oct}', callback_data='oct_days_off')
    nov_button = InlineKeyboardButton(text=f'{nov}', callback_data='nov_days_off')
    dec_button = InlineKeyboardButton(text=f'{dec}', callback_data='dec_days_off')

    keyboard.row(jan_button, feb_button, mar_button)
    keyboard.row(apr_button, may_button, june_button)
    keyboard.row(jul_button, aug_button, sep_button)
    keyboard.row(oct_button, nov_button, dec_button)
    await bot.send_message(callback_query.from_user.id, "📅 Выберите месяц:", reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data in ['jan_days_off'])
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Январе 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)
    await Form.district.set()

    norm_working_days = 17
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)

    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {jan}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {jan}:</code><b> {norm_working_days*8}</b>\n"
                                  f"\n<code>📅 Выходные:</code><b>14, 15, 21, 22, 28, 29</b>\n"
                                  f"<code>📅 Праздничные:</code><b> 1, 2, 3, 4, 5, 6, 7, 8</b>\n"
                                  f"\n<code>📅 Выходные поверхность:</code><b>1, 2, 3, 4, 5, 6, 7, 8, 14, 15, 21, 22, 28, 29</b>\n"
                                  f"<code>📅 Выходные подземные:</code><b>1, 2, 3, 4, 5, 6, 7, 8, 11, 15, 18, 22, 25, 29</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML")

    await state.finish()


@dp.callback_query_handler(lambda c: c.data in ['feb_days_off'])
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Феврале 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)
    await Form.district.set()

    norm_working_days = 18
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)

    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {feb}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {feb}:</code><b> {norm_working_days*8}</b>\n"
                                  f"\n<code>📅 Выходные:</code><b>4, 5, 11, 12, 18, 19, 23, 23, 25, 26</b>\n"
                                  f"<code>📅 Праздничные:</code><b> 23</b>\n"
                                  f"\n<code>📅 Выходные поверхность:</code><b>4, 5, 11, 12, 18, 19, 23, 24, 25, 26</b>\n"
                                  f"<code>📅 Выходные подземные:</code><b>1, 5, 8, 12, 15, 19, 22, 23, 24, 26</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML")

    await state.finish()


@dp.callback_query_handler(lambda c: c.data in ['mar_days_off'])
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Марте 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)
    await Form.district.set()

    norm_working_days = 22
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)

    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {mar}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {mar}:</code><b> {norm_working_days*8}</b>\n"
                                  f"\n<code>📅 Выходные:</code><b>4, 5, 11, 12, 18, 19, 25, 26</b>\n"
                                  f"<code>📅 Праздничные:</code><b> 8</b>\n"
                                  f"\n<code>📅 Выходные поверхность:</code><b>4, 5, 8, 11, 12, 18, 19, 25, 26</b>\n"
                                  f"<code>📅 Выходные подземные:</code><b>1, 5, 8, 12, 15, 19, 22, 26, 29</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML")

    await state.finish()


@dp.callback_query_handler(lambda c: c.data in ['apr_days_off'])
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Апреле 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)
    await Form.district.set()

    norm_working_days = 19
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)

    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {apr}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {apr}:</code><b> {norm_working_days*8}</b>\n"
                                  f"\n<code>📅 Выходные:</code><b>1, 2, 8, 9, 15, 16, 17, 22, 23, 29, 30</b>\n"
                                  f"<code>📅 Праздничные:</code><b>7</b>\n"
                                  f"\n<code>📅 Выходные поверхность:</code><b>1, 2, 8, 9, 15, 16, 17, 22, 23, 29, 30</b>\n"
                                  f"<code>📅 Выходные подземные:</code><b>1, 2, 5, 9, 12, 16, 17, 19, 23, 26, 30</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML")

    await state.finish()


@dp.callback_query_handler(lambda c: c.data in ['may_days_off'])
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Мае 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)
    await Form.district.set()

    norm_working_days = 19
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)

    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {may}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {may}:</code><b> {norm_working_days*8}</b>\n"
                                  f"\n<code>📅 Выходные:</code><b> 6, 7, 8, 13, 14, 20, 21, 27, 28</b>\n"
                                  f"<code>📅 Праздничные:</code><b> 1, 9, 11</b>\n"
                                  f"\n<code>📅 Выходные поверхность:</code><b> 1, 6, 7, 8, 9, 10, 13, 14, 20, 21, 27, 28</b>\n"
                                  f"<code>📅 Выходные подземные:</code><b>1, 3, 7, 8, 9, 11, 14, 17, 21, 24, 28</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML")

    await state.finish()


@dp.callback_query_handler(lambda c: c.data in ['june_days_off'])
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Июне 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)
    await Form.district.set()

    norm_working_days = 20
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)

    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {june}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {june}:</code><b> {norm_working_days*8}</b>\n"
                                  f"\n<code>📅 Выходные:</code><b>3, 4, 5, 10, 11, 12, 17, 18, 24, 25</b>\n"
                                  f"<code>📅 Праздничные:</code><b> 5, 12</b>\n"
                                  f"\n<code>📅 Выходные поверхность:</code><b>3, 4, 5, 10, 11, 12, 17, 18, 24, 25</b>\n"
                                  f"<code>📅 Выходные подземные:</code><b>4, 5, 7, 11, 12, 14, 18, 21, 25, 28</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML")

    await state.finish()


@dp.callback_query_handler(lambda c: c.data in ['jul_days_off'])
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Июле 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)
    await Form.district.set()

    norm_working_days = 21
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)

    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {jul}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {jul}:</code><b> {norm_working_days*8}</b>\n"
                                  f"\n<code>📅 Выходные:</code><b>1, 2, 8, 9, 15, 16, 22, 23, 29, 30</b>\n"
                                  f"<code>📅 Праздничные:</code><b> -</b>\n"
                                  f"\n<code>📅 Выходные поверхность:</code><b>1, 2, 8, 9, 15, 16, 22, 23, 29, 30</b>\n"
                                  f"<code>📅 Выходные подземные:</code><b>1, 2, 5, 9, 12, 16, 29, 23, 26, 30</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML")

    await state.finish()


@dp.callback_query_handler(lambda c: c.data in ['aug_days_off'])
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Августе 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)
    await Form.district.set()

    norm_working_days = 23
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)

    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {aug}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {aug}:</code><b> {norm_working_days*8}</b>\n"
                                  f"\n<code>📅 Выходные:</code><b>5, 6, 12, 13, 19, 20, 26, 27</b>\n"
                                  f"<code>📅 Праздничные:</code><b> -</b>\n"
                                  f"\n<code>📅 Выходные поверхность:</code><b>5, 6, 12, 13, 19, 20, 26, 27</b>\n"
                                  f"<code>📅 Выходные подземные:</code><b>2, 6, 9, 13, 16, 20, 23, 27</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML")

    await state.finish()


@dp.callback_query_handler(lambda c: c.data in ['sep_days_off'])
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Сентябре 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)
    await Form.district.set()

    norm_working_days = 21
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)

    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {sep}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {sep}:</code><b> {norm_working_days*8}</b>\n"
                                  f"\n<code>📅 Выходные:</code><b> 2, 3, 9, 10, 16, 17, 23, 24, 30</b>\n"
                                  f"<code>📅 Праздничные:</code><b> -</b>\n"
                                  f"\n<code>📅 Выходные поверхность:</code><b> 2, 3, 9, 10, 16, 17, 23, 24, 30</b>\n"
                                  f"<code>📅 Выходные подземные:</code><b>2, 3, 6, 10, 13, 17, 20, 24, 27</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML")

    await state.finish()


@dp.callback_query_handler(lambda c: c.data in ['oct_days_off'])
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Октябре 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)
    await Form.district.set()

    norm_working_days = 21
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)

    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {oct}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {oct}:</code><b> {norm_working_days*8}</b>\n"
                                  f"\n<code>📅 Выходные:</code><b> 1, 2, 7, 8, 14, 15, 21, 22, 28, 29</b>\n"
                                  f"<code>📅 Праздничные:</code><b> -</b>\n"
                                  f"\n<code>📅 Выходные поверхность:</code><b> 1, 2, 7, 8, 14, 15, 21, 22, 28, 29</b>\n"
                                  f"<code>📅 Выходные подземные:</code><b>1, 2, 4, 8 11, 15, 18, 22, 25, 29</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML")

    await state.finish()


@dp.callback_query_handler(lambda c: c.data in ['nov_days_off'])
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Ноябре 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)
    await Form.district.set()

    norm_working_days = 21
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)

    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {nov}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {nov}:</code><b> {norm_working_days*8}</b>\n"
                                  f"\n<code>📅 Выходные:</code><b> 5, 6, 11, 12, 18, 19, 25, 26</b>\n"
                                  f"<code>📅 Праздничные:</code><b> 4</b>\n"
                                  f"\n<code>📅 Выходные поверхность:</code><b>4, 5, 6, 11, 12, 18, 19, 25, 26</b>\n"
                                  f"<code>📅 Выходные подземные:</code><b>1, 5, 6, 12, 15, 19, 22, 26, 29</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML")

    await state.finish()


@dp.callback_query_handler(lambda c: c.data in ['dec_days_off'])
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Декабре 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)
    await Form.district.set()

    norm_working_days = 21
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)

    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {dec}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {dec}:</code><b> {norm_working_days*8}</b>\n"
                                  f"\n<code>📅 Выходные:</code><b> 2, 3, 9, 10, 16, 17, 23, 24, 30, 31</b>\n"
                                  f"<code>📅 Праздничные:</code><b> -</b>\n"
                                  f"\n<code>📅 Выходные поверхность:</code><b> 2, 3, 9, 10, 16, 17, 23, 24, 30, 31</b>\n"
                                  f"<code>📅 Выходные подземные:</code><b>2, 3, 6, 10, 13, 17, 20, 24, 27, 31</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML")

    await state.finish()
