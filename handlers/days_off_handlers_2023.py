import math

from aiogram import types, F
from aiogram.fsm.context import FSMContext

from keyboards.welcome_keyboard import keyboard_go_back, work_on_days_off_2023
from system.global_variables import jan, feb, mar, apr, may, june, jul, aug, sep, nov, dec
from system.system import dp, bot, router


@router.callback_query(F.data == "days_off")
async def days_off_callback_month(callback_query: types.CallbackQuery):
    """Плановые и выходные дни в Мае 2023"""
    await bot.send_message(callback_query.from_user.id, "📅 Выберите месяц:", reply_markup=work_on_days_off_2023())

@router.callback_query(F.data == "working_days_per_year")
async def working_days_per_year_process_callback(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Январе 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)

    jan_2023 = 17  # 01
    feb_2023 = 18  # 02
    mar_2023 = 22  # 03
    apr_2023 = 19  # 04
    may_2023 = 19  # 05
    jun_2023 = 20  # 06
    jul_2023 = 21  # 07
    aug_2023 = 23  # 08
    sep_2023 = 21  # 09
    oct_2023 = 21  # 10
    nov_2023 = 21  # 11
    dec_2023 = 21  # 12
    days_all = (jan_2023 + feb_2023 + mar_2023 + apr_2023 + may_2023 + jun_2023 +
                jul_2023 + aug_2023 + sep_2023 + oct_2023 + nov_2023 + dec_2023)
    markup = keyboard_go_back()  # Клавиатура возврата в начальное меню
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f"<code>Количество рабочих дней в 2023 году</code>\n"
                                  f"\n<code>Январь: {jan_2023}</code>\n"
                                  f"<code>Февраль: {feb_2023}</code>\n"
                                  f"<code>Март: {mar_2023}</code>\n"
                                  f"<code>Апрель: {apr_2023}</code>\n"
                                  f"<code>Май: {may_2023}</code>\n"
                                  f"<code>Июнь: {jun_2023}</code>\n"
                                  f"<code>Июль: {jul_2023}</code>\n"
                                  f"<code>Август: {aug_2023}</code>\n"
                                  f"<code>Сентябрь: {sep_2023}</code>\n"
                                  f"<code>Октябрь: {oct_2023}</code>\n"
                                  f"<code>Ноябрь: {nov_2023}</code>\n"
                                  f"<code>Декабрь: {dec_2023}</code>\n"
                                  f"\n<code>Всего: {days_all}</code>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML", reply_markup=markup)
    await state.clear()

@router.callback_query(F.data == "jan_days_off")
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Январе 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)

    norm_working_days = 17
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)

    markup = keyboard_go_back()  # Клавиатура возврата в начальное меню
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {jan}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {jan}:</code><b> {norm_working_days * 8}</b>\n"
                                  f"\n<code>📅 Выходные:</code><b>14, 15, 21, 22, 28, 29</b>\n"
                                  f"<code>📅 Праздничные:</code><b> 1, 2, 3, 4, 5, 6, 7, 8</b>\n"
                                  f"\n<code>📅 Выходные поверхность:</code><b>1, 2, 3, 4, 5, 6, 7, 8, 14, 15, 21, 22, 28, 29</b>\n"
                                  f"<code>📅 Выходные подземные:</code><b>1, 2, 3, 4, 5, 6, 7, 8, 11, 15, 18, 22, 25, 29</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML", reply_markup=markup)
    await state.clear()

@router.callback_query(F.data == "feb_days_off")
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Феврале 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)

    norm_working_days = 18
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)
    markup = keyboard_go_back()  # Клавиатура возврата в начальное меню
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {feb}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {feb}:</code><b> {norm_working_days * 8}</b>\n"
                                  f"\n<code>📅 Выходные:</code><b>4, 5, 11, 12, 18, 19, 23, 23, 25, 26</b>\n"
                                  f"<code>📅 Праздничные:</code><b> 23</b>\n"
                                  f"\n<code>📅 Выходные поверхность:</code><b>4, 5, 11, 12, 18, 19, 23, 24, 25, 26</b>\n"
                                  f"<code>📅 Выходные подземные:</code><b>1, 5, 8, 12, 15, 19, 22, 23, 24, 26</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML", reply_markup=markup)
    await state.clear()

@router.callback_query(F.data == "mar_days_off")
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Марте 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)

    norm_working_days = 22
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)
    markup = keyboard_go_back()  # Клавиатура возврата в начальное меню
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {mar}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {mar}:</code><b> {norm_working_days * 8}</b>\n"
                                  f"\n<code>📅 Выходные:</code><b>4, 5, 11, 12, 18, 19, 25, 26</b>\n"
                                  f"<code>📅 Праздничные:</code><b> 8</b>\n"
                                  f"\n<code>📅 Выходные поверхность:</code><b>4, 5, 8, 11, 12, 18, 19, 25, 26</b>\n"
                                  f"<code>📅 Выходные подземные:</code><b>1, 5, 8, 12, 15, 19, 22, 26, 29</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML", reply_markup=markup)
    await state.clear()

@router.callback_query(F.data == "apr_days_off")
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Апреле 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)

    norm_working_days = 19
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)
    markup = keyboard_go_back()  # Клавиатура возврата в начальное меню
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {apr}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {apr}:</code><b> {norm_working_days * 8}</b>\n"
                                  f"\n<code>📅 Выходные:</code><b>1, 2, 8, 9, 15, 16, 17, 22, 23, 29, 30</b>\n"
                                  f"<code>📅 Праздничные:</code><b>7</b>\n"
                                  f"\n<code>📅 Выходные поверхность:</code><b>1, 2, 8, 9, 15, 16, 17, 22, 23, 29, 30</b>\n"
                                  f"<code>📅 Выходные подземные:</code><b>1, 2, 5, 9, 12, 16, 17, 19, 23, 26, 30</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML", reply_markup=markup)
    await state.clear()

@router.callback_query(F.data == "may_days_off")
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Мае 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)

    norm_working_days = 19
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)
    markup = keyboard_go_back()  # Клавиатура возврата в начальное меню
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {may}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {may}:</code><b> {norm_working_days * 8}</b>\n"
                                  f"\n<code>📅 Выходные:</code><b> 6, 7, 8, 13, 14, 20, 21, 27, 28</b>\n"
                                  f"<code>📅 Праздничные:</code><b> 1, 9, 11</b>\n"
                                  f"\n<code>📅 Выходные поверхность:</code><b> 1, 6, 7, 8, 9, 11, 13, 14, 20, 21, 27, 28</b>\n"
                                  f"<code>📅 Выходные подземные:</code><b>1, 3, 7, 8, 9, 11, 14, 17, 21, 24, 28</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML", reply_markup=markup)
    await state.clear()

@router.callback_query(F.data == "june_days_off")
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Июне 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)

    norm_working_days = 20
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)
    markup = keyboard_go_back()  # Клавиатура возврата в начальное меню
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {june}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {june}:</code><b> {norm_working_days * 8}</b>\n"
                                  f"\n<code>📅 Выходные:</code><b>3, 4, 5, 10, 11, 12, 17, 18, 24, 25</b>\n"
                                  f"<code>📅 Праздничные:</code><b> 5, 12</b>\n"
                                  f"\n<code>📅 Выходные поверхность:</code><b>3, 4, 5, 10, 11, 12, 17, 18, 24, 25</b>\n"
                                  f"<code>📅 Выходные подземные:</code><b>4, 5, 7, 11, 12, 14, 18, 21, 25, 28</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML", reply_markup=markup)
    await state.clear()

@router.callback_query(F.data == "jul_days_off")
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Июле 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)

    norm_working_days = 21
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)
    markup = keyboard_go_back()  # Клавиатура возврата в начальное меню
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {jul}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {jul}:</code><b> {norm_working_days * 8}</b>\n"
                                  f"\n<code>📅 Выходные:</code><b>1, 2, 8, 9, 15, 16, 22, 23, 29, 30</b>\n"
                                  f"<code>📅 Праздничные:</code><b> -</b>\n"
                                  f"\n<code>📅 Выходные поверхность:</code><b>1, 2, 8, 9, 15, 16, 22, 23, 29, 30</b>\n"
                                  f"<code>📅 Выходные подземные:</code><b>1, 2, 5, 9, 12, 16, 29, 23, 26, 30</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML", reply_markup=markup)
    await state.clear()

@router.callback_query(F.data == "aug_days_off")
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Августе 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)

    norm_working_days = 23
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)
    markup = keyboard_go_back()  # Клавиатура возврата в начальное меню
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {aug}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {aug}:</code><b> {norm_working_days * 8}</b>\n"
                                  f"\n<code>📅 Выходные:</code><b>5, 6, 12, 13, 19, 20, 26, 27</b>\n"
                                  f"<code>📅 Праздничные:</code><b> -</b>\n"
                                  f"\n<code>📅 Выходные поверхность:</code><b>5, 6, 12, 13, 19, 20, 26, 27</b>\n"
                                  f"<code>📅 Выходные подземные:</code><b>2, 6, 9, 13, 16, 20, 23, 27</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML", reply_markup=markup)
    await state.clear()

@router.callback_query(F.data == "sep_days_off")
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Сентябре 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)

    norm_working_days = 21
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)
    markup = keyboard_go_back()  # Клавиатура возврата в начальное меню
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {sep}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {sep}:</code><b> {norm_working_days * 8}</b>\n"
                                  f"\n<code>📅 Выходные:</code><b> 2, 3, 9, 10, 16, 17, 23, 24, 30</b>\n"
                                  f"<code>📅 Праздничные:</code><b> -</b>\n"
                                  f"\n<code>📅 Выходные поверхность:</code><b> 2, 3, 9, 10, 16, 17, 23, 24, 30</b>\n"
                                  f"<code>📅 Выходные подземные:</code><b>2, 3, 6, 10, 13, 17, 20, 24, 27</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML", reply_markup=markup)
    await state.clear()

@router.callback_query(F.data == "oct_days_off")
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Октябре 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)

    norm_working_days = 21
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)
    markup = keyboard_go_back()  # Клавиатура возврата в начальное меню
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {oct}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {oct}:</code><b> {norm_working_days * 8}</b>\n"
                                  f"\n<code>📅 Выходные:</code><b> 1, 2, 7, 8, 14, 15, 21, 22, 28, 29</b>\n"
                                  f"<code>📅 Праздничные:</code><b> -</b>\n"
                                  f"\n<code>📅 Выходные поверхность:</code><b> 1, 2, 7, 8, 14, 15, 21, 22, 28, 29</b>\n"
                                  f"<code>📅 Выходные подземные:</code><b>1, 2, 4, 8 11, 15, 18, 22, 25, 29</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML", reply_markup=markup)
    await state.clear()

@router.callback_query(F.data == "nov_days_off")
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Ноябре 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)

    norm_working_days = 21
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)
    markup = keyboard_go_back()  # Клавиатура возврата в начальное меню
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {nov}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {nov}:</code><b> {norm_working_days * 8}</b>\n"
                                  f"\n<code>📅 Выходные:</code><b> 5, 6, 11, 12, 18, 19, 25, 26</b>\n"
                                  f"<code>📅 Праздничные:</code><b> 4</b>\n"
                                  f"\n<code>📅 Выходные поверхность:</code><b>4, 5, 6, 11, 12, 18, 19, 25, 26</b>\n"
                                  f"<code>📅 Выходные подземные:</code><b>1, 5, 6, 12, 15, 19, 22, 26, 29</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML", reply_markup=markup)
    await state.clear()

@router.callback_query(F.data == "dec_days_off")
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Декабре 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)

    norm_working_days = 21
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)
    markup = keyboard_go_back()  # Клавиатура возврата в начальное меню
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в {dec}:</code><b> {norm_working_days}</b>\n"
                                  f"<code>✅ Норма времени в {dec}:</code><b> {norm_working_days * 8}</b>\n"
                                  f"\n<code>📅 Выходные:</code><b> 2, 3, 9, 10, 16, 17, 23, 24, 30, 31</b>\n"
                                  f"<code>📅 Праздничные:</code><b> -</b>\n"
                                  f"\n<code>📅 Выходные поверхность:</code><b> 2, 3, 9, 10, 16, 17, 23, 24, 30, 31</b>\n"
                                  f"<code>📅 Выходные подземные:</code><b>2, 3, 6, 10, 13, 17, 20, 24, 27, 31</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML", reply_markup=markup)
    await state.clear()


def register_days_off_callback_month_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(days_off_callback_month)
