import codecs
import json

from aiogram import types, F
from aiogram.fsm.context import FSMContext
from loguru import logger

from handlers.days_off_handlers_2024 import counting_working_days
from keyboards.welcome_keyboard import keyboard_go_back, work_on_days_off_2025
from system.system import dp, bot, router


def reading_JSON_file():
    """Считываем файл с датами"""
    with codecs.open('settings/days_off_2025.json', 'rb') as f:
        data = json.load(f)
        logger.info(data)
    return data


def list_of_weekends_for_a_month(data, month_json, norm_working_hours, norm_hours_12h_shift,
                                 norm_hours_24h_shift):
    """"Список выходных дней в месяце"""
    try:
        text = (
            f'\n{data[f"{month_json}"][0]}\n'

            f'\n<code>✅ Норма выходов:</code><b> {data[f"{month_json}"][1]}</b>'
            f'\n<code>✅ Норма времени:</code><b> {norm_working_hours}</b>'
            # f'\n<code>📅 Выходные:</code><b>13, 14, 20, 21, 27, 28</b>'
            f'\n\n<code>📅 Праздничные:</code><b> {data[f"{month_json}"][2]}</b>'
            # f'\n<code>📅 Выходные дни:</code><b>1, 2, 3, 4, 5, 6, 7, 8, 13, 14, 20, 21, 27, 28</b>'
            f'\n\n<code>🔨 Выходов для 6 часовых:</code><b> {data[f"{month_json}"][1]}</b>'
            f'\n<code>🔨 Выходов для 8 часовых:</code><b> {data[f"{month_json}"][1]}</b>'
            f'\n<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>'
            f'\n<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n'

            f'\nНажмите /start, чтобы вернуться в начало'
        )
        return text
    except Exception as e:
        logger.exception(e)


@router.callback_query(F.data == "days_off_25")
async def days_off_callback_month_2025(callback_query: types.CallbackQuery):
    """Плановые и выходные дни в 2025"""
    try:
        data = reading_JSON_file()
        await bot.edit_message_text(
            chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
            text=f"Продолжительность рабочего времени в ДНР на 2025 год"
                 "\n\n📅 Выберите месяц:",
            reply_markup=work_on_days_off_2025(data)
        )
    except Exception as e:
        logger.error(e)


@router.callback_query(F.data == "working_days_per_year_2025")
async def working_days_per_year_process_callback_2025(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Январе 2025"""
    try:
        await state.update_data(month=callback_query.data)
        data = reading_JSON_file()
        days_all = (int(data["jan_2025"][1]) + int(data["feb_2025"][1]) + int(data["mar_2025"][1]) + int(
            data["apr_2025"][1]) + int(data["may_2025"][1]) + int(data["june_2025"][1]) +
                    int(data["jul_2025"][1]) + int(data["aug_2025"][1]) + int(data["sep_2025"][1]) + int(
                    data["oct_2025"][1]) + int(data["nov_2025"][1]) + int(data["dec_2025"][1]))
        markup = keyboard_go_back()  # Клавиатура возврата в начальное меню
        # добавляем разметку в сообщение
        response_message = callback_query.message
        await response_message.answer(f'<code>Количество рабочих дней в 2025 году</code>\n'
                                      f'\n<code>Январь: {data["jan_2025"][1]}</code>\n'
                                      f'<code>Февраль: {data["feb_2025"][1]}</code>\n'
                                      f'<code>Март: {data["mar_2025"][1]}</code>\n'
                                      f'<code>Апрель: {data["apr_2025"][1]}</code>\n'
                                      f'<code>Май: {data["may_2025"][1]}</code>\n'
                                      f'<code>Июнь: {data["june_2025"][1]}</code>\n'
                                      f'<code>Июль: {data["jul_2025"][1]}</code>\n'
                                      f'<code>Август: {data["aug_2025"][1]}</code>\n'
                                      f'<code>Сентябрь: {data["sep_2025"][1]}</code>\n'
                                      f'<code>Октябрь: {data["oct_2025"][1]}</code>\n'
                                      f'<code>Ноябрь: {data["nov_2025"][1]}</code>\n'
                                      f'<code>Декабрь: {data["dec_2025"][1]}</code>\n'
                                      f'\n<code>Всего: {days_all}</code>\n'
                                      f'\nНажмите /start, чтобы вернуться в начало', parse_mode="HTML",
                                      reply_markup=markup)
        await state.clear()
    except Exception as e:
        logger.error(e)


@router.callback_query(F.data == "jan_days_off_2025")
async def days_off_process_callback_monthh_2025(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Январе 2025"""
    try:
        await state.update_data(month=callback_query.data)
        data = reading_JSON_file()
        norm_working_hours, norm_hours_12h_shift, norm_hours_24h_shift = counting_working_days(data["jan_2025"][1])
        # добавляем разметку в сообщение
        text = list_of_weekends_for_a_month(data, 'jan_2025', norm_working_hours, norm_hours_12h_shift,
                                            norm_hours_24h_shift)
        await bot.edit_message_text(
            chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
            text=text, parse_mode="HTML",
            reply_markup=keyboard_go_back()  # Клавиатура возврата в начальное меню
        )
        await state.clear()
    except Exception as e:
        logger.exception(e)


@router.callback_query(F.data == "feb_days_off_2025")
async def days_off_process_callback_monthh_2025(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Феврале 2025"""
    await state.update_data(month=callback_query.data)
    data = reading_JSON_file()
    norm_working_hours, norm_hours_12h_shift, norm_hours_24h_shift = counting_working_days(data["feb_2025"][1])
    # добавляем разметку в сообщение
    text = list_of_weekends_for_a_month(data, 'feb_2025', norm_working_hours, norm_hours_12h_shift,
                                        norm_hours_24h_shift)
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        text=text, parse_mode="HTML",
        reply_markup=keyboard_go_back()  # Клавиатура возврата в начальное меню
    )
    await state.clear()


@router.callback_query(F.data == "mar_days_off_2025")
async def days_off_process_callback_monthh_2025(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Марте 2025"""
    await state.update_data(month=callback_query.data)
    data = reading_JSON_file()
    norm_working_hours, norm_hours_12h_shift, norm_hours_24h_shift = counting_working_days(data["mar_2025"][1])
    # добавляем разметку в сообщение
    text = list_of_weekends_for_a_month(data, 'mar_2025', norm_working_hours, norm_hours_12h_shift,
                                        norm_hours_24h_shift)
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        text=text, parse_mode="HTML",
        reply_markup=keyboard_go_back()  # Клавиатура возврата в начальное меню
    )
    await state.clear()


@router.callback_query(F.data == "apr_days_off_2025")
async def days_off_process_callback_monthh_2025(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Апреле 2025"""
    await state.update_data(month=callback_query.data)
    data = reading_JSON_file()
    norm_working_hours, norm_hours_12h_shift, norm_hours_24h_shift = counting_working_days(data["apr_2025"][1])
    # добавляем разметку в сообщение
    text = list_of_weekends_for_a_month(data, 'apr_2025', norm_working_hours, norm_hours_12h_shift,
                                        norm_hours_24h_shift)
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        text=text, parse_mode="HTML",
        reply_markup=keyboard_go_back()  # Клавиатура возврата в начальное меню
    )
    await state.clear()


@router.callback_query(F.data == "may_days_off_2025")
async def days_off_process_callback_monthh_2025(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Мае 2025"""
    await state.update_data(month=callback_query.data)
    data = reading_JSON_file()
    norm_working_hours, norm_hours_12h_shift, norm_hours_24h_shift = counting_working_days(data["may_2025"][1])
    # добавляем разметку в сообщение
    text = list_of_weekends_for_a_month(data, 'may_2025', norm_working_hours, norm_hours_12h_shift,
                                        norm_hours_24h_shift)
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        text=text, parse_mode="HTML",
        reply_markup=keyboard_go_back()  # Клавиатура возврата в начальное меню
    )
    await state.clear()


@router.callback_query(F.data == "june_days_off_2025")
async def days_off_process_callback_monthh_2025(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Июне 2025"""
    await state.update_data(month=callback_query.data)
    data = reading_JSON_file()
    norm_working_hours, norm_hours_12h_shift, norm_hours_24h_shift = counting_working_days(data["june_2025"][1])
    # добавляем разметку в сообщение
    text = list_of_weekends_for_a_month(data, 'june_2025', norm_working_hours, norm_hours_12h_shift,
                                        norm_hours_24h_shift)
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        text=text, parse_mode="HTML",
        reply_markup=keyboard_go_back()  # Клавиатура возврата в начальное меню
    )
    await state.clear()


@router.callback_query(F.data == "jul_days_off_2025")
async def days_off_process_callback_monthh_2025(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Июле 2025"""
    await state.update_data(month=callback_query.data)
    data = reading_JSON_file()
    norm_working_hours, norm_hours_12h_shift, norm_hours_24h_shift = counting_working_days(data["jul_2025"][1])
    # добавляем разметку в сообщение
    text = list_of_weekends_for_a_month(data, 'jul_2025', norm_working_hours, norm_hours_12h_shift,
                                        norm_hours_24h_shift)
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        text=text, parse_mode="HTML",
        reply_markup=keyboard_go_back()  # Клавиатура возврата в начальное меню
    )
    await state.clear()


@router.callback_query(F.data == "aug_days_off_2025")
async def days_off_process_callback_monthh_2025(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Августе 2025"""
    await state.update_data(month=callback_query.data)
    data = reading_JSON_file()
    norm_working_hours, norm_hours_12h_shift, norm_hours_24h_shift = counting_working_days(data["aug_2025"][1])
    # добавляем разметку в сообщение
    text = list_of_weekends_for_a_month(data, 'aug_2025', norm_working_hours, norm_hours_12h_shift,
                                        norm_hours_24h_shift)
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        text=text, parse_mode="HTML",
        reply_markup=keyboard_go_back()  # Клавиатура возврата в начальное меню
    )
    await state.clear()


@router.callback_query(F.data == "sep_days_off_2025")
async def days_off_process_callback_monthh_2025(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Сентябре 2025"""
    await state.update_data(month=callback_query.data)
    data = reading_JSON_file()
    norm_working_hours, norm_hours_12h_shift, norm_hours_24h_shift = counting_working_days(data["sep_2025"][1])
    # добавляем разметку в сообщение
    text = list_of_weekends_for_a_month(data, 'sep_2025', norm_working_hours, norm_hours_12h_shift,
                                        norm_hours_24h_shift)
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        text=text, parse_mode="HTML",
        reply_markup=keyboard_go_back()  # Клавиатура возврата в начальное меню
    )
    await state.clear()


@router.callback_query(F.data == "oct_days_off_2025")
async def days_off_process_callback_monthh_2025(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Октябре 2025"""
    await state.update_data(month=callback_query.data)
    data = reading_JSON_file()
    norm_working_hours, norm_hours_12h_shift, norm_hours_24h_shift = counting_working_days(data["oct_2025"][1])
    # добавляем разметку в сообщение
    text = list_of_weekends_for_a_month(data, 'oct_2025', norm_working_hours, norm_hours_12h_shift,
                                        norm_hours_24h_shift)
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        text=text, parse_mode="HTML",
        reply_markup=keyboard_go_back()  # Клавиатура возврата в начальное меню
    )
    await state.clear()


@router.callback_query(F.data == "nov_days_off_2025")
async def days_off_process_callback_monthh_2025(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Ноябре 2025"""
    await state.update_data(month=callback_query.data)
    data = reading_JSON_file()
    norm_working_hours, norm_hours_12h_shift, norm_hours_24h_shift = counting_working_days(data["nov_2025"][1])
    # добавляем разметку в сообщение
    text = list_of_weekends_for_a_month(data, 'nov_2025', norm_working_hours, norm_hours_12h_shift,
                                        norm_hours_24h_shift)
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        text=text, parse_mode="HTML",
        reply_markup=keyboard_go_back()  # Клавиатура возврата в начальное меню
    )
    await state.clear()


@router.callback_query(F.data == "dec_days_off_2025")
async def days_off_process_callback_monthh_2025(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Декабре 2025"""
    await state.update_data(month=callback_query.data)
    data = reading_JSON_file()
    norm_working_hours, norm_hours_12h_shift, norm_hours_24h_shift = counting_working_days(data["dec_2025"][1])
    text = list_of_weekends_for_a_month(data, 'dec_2025', norm_working_hours, norm_hours_12h_shift,
                                        norm_hours_24h_shift)
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
        text=text, parse_mode="HTML",
        reply_markup=keyboard_go_back()  # Клавиатура возврата в начальное меню
    )
    await state.clear()


def register_days_off_callback_month_handler_2025():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(days_off_callback_month_2025)
