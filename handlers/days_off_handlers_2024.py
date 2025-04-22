# -*- coding: utf-8 -*-
import codecs
import json
import math

from aiogram import types, F
from aiogram.fsm.context import FSMContext
from loguru import logger

from keyboards.welcome_keyboard import keyboard_go_back, work_on_days_off_2024
from system.global_variables import *
from system.system import dp, bot, router


@router.callback_query(F.data == "days_off_24")
async def days_off_callback_month_2024(callback_query: types.CallbackQuery):
    """Плановые и выходные дни в 2024"""
    try:
        with codecs.open('settings/days_off_2024.json', 'rb') as f:
            data = json.load(f)
            logger.info(data)

        keyboard = work_on_days_off_2024(data)

        await bot.edit_message_text(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            text="📅 Выберите месяц:",
            reply_markup=keyboard
        )
    except Exception as e:
        logger.error(e)


@router.callback_query(F.data == "working_days_per_year_2024")
async def working_days_per_year_process_callback_2024(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Январе 2023"""
    try:
        selected_month = callback_query.data
        await state.update_data(month=selected_month)

        with codecs.open('settings/days_off_2024.json', 'rb') as f:
            data = json.load(f)
            logger.info(data)

        days_all = (int(data["jan_2024"][1]) + int(data["feb_2024"][1]) + int(data["mar_2024"][1]) + int(
            data["apr_2024"][1]) + int(data["may_2024"][1]) + int(data["june_2024"][1]) +
                    int(data["jul_2024"][1]) + int(data["aug_2024"][1]) + int(data["sep_2024"][1]) + int(
                    data["oct_2024"][1]) + int(data["nov_2024"][1]) + int(data["dec_2024"][1]))
        markup = keyboard_go_back()  # Клавиатура возврата в начальное меню
        # добавляем разметку в сообщение
        response_message = callback_query.message
        await response_message.answer(f'<code>Количество рабочих дней в 2024 году</code>\n'
                                      f'\n<code>Январь: {data["jan_2024"][1]}</code>\n'
                                      f'<code>Февраль: {data["feb_2024"][1]}</code>\n'
                                      f'<code>Март: {data["mar_2024"][1]}</code>\n'
                                      f'<code>Апрель: {data["apr_2024"][1]}</code>\n'
                                      f'<code>Май: {data["may_2024"][1]}</code>\n'
                                      f'<code>Июнь: {data["june_2024"][1]}</code>\n'
                                      f'<code>Июль: {data["jul_2024"][1]}</code>\n'
                                      f'<code>Август: {data["aug_2024"][1]}</code>\n'
                                      f'<code>Сентябрь: {data["sep_2024"][1]}</code>\n'
                                      f'<code>Октябрь: {data["oct_2024"][1]}</code>\n'
                                      f'<code>Ноябрь: {data["nov_2024"][1]}</code>\n'
                                      f'<code>Декабрь: {data["dec_2024"][1]}</code>\n'
                                      f'\n<code>Всего: {days_all}</code>\n'
                                      f'\nНажмите /start, чтобы вернуться в начало', parse_mode="HTML",
                                      reply_markup=markup)
        await state.clear()
    except Exception as e:
        logger.error(e)


def counting_working_days(norm_working_days):
    """Подсчет рабочих дней в месяце для: 8, 12, 24 часовиков"""
    norm_working_hours = int(norm_working_days) * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)
    return norm_working_hours, norm_hours_12h_shift, norm_hours_24h_shift


@router.callback_query(F.data == "jan_days_off_2024")
async def days_off_process_callback_monthh_2024(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Январе 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)

    with codecs.open('settings/days_off_2024.json', 'rb') as f:
        data = json.load(f)
        logger.info(data)

    norm_working_hours, norm_hours_12h_shift, norm_hours_24h_shift = counting_working_days(data["jan_2024"][1])

    markup = keyboard_go_back()  # Клавиатура возврата в начальное меню
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f'<code>✅ Норма выходов в {jan}:</code><b> {data["jan_2024"][1]}</b>\n'
                                  f'<code>✅ Норма времени в {jan}:</code><b> {norm_working_hours}</b>\n'
                                  f'\n<code>📅 Выходные:</code><b>13, 14, 20, 21, 27, 28</b>\n'
                                  f'<code>📅 Праздничные:</code><b> {data["jan_2024"][2]}</b>\n'
                                  f'\n<code>📅 Выходные дни:</code><b>1, 2, 3, 4, 5, 6, 7, 8, 13, 14, 20, 21, 27, 28</b>\n'
                                  f'\n<code>🔨 Выходов для 6 часовых:</code><b> {data["jan_2024"][1]}</b>\n'
                                  f'<code>🔨 Выходов для 8 часовых:</code><b> {data["jan_2024"][1]}</b>\n'
                                  f'<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n'
                                  f'<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n'
                                  f'\nНажмите /start, чтобы вернуться в начало', parse_mode="HTML", reply_markup=markup)
    await state.clear()


@router.callback_query(F.data == "feb_days_off_2024")
async def days_off_process_callback_monthh_2024(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Феврале 2024"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)

    with codecs.open('settings/days_off_2024.json', 'rb') as f:
        data = json.load(f)
        logger.info(data)

    norm_working_hours, norm_hours_12h_shift, norm_hours_24h_shift = counting_working_days(data["feb_2024"][1])
    markup = keyboard_go_back()  # Клавиатура возврата в начальное меню
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f'<code>✅ Норма выходов в {feb}:</code><b> {data["feb_2024"][1]}</b>\n'
                                  f'<code>✅ Норма времени в {feb}:</code><b> {norm_working_hours}</b>\n'
                                  f'\n<code>📅 Выходные:</code><b>4, 5, 11, 12, 18, 19, 23, 23, 25, 26</b>\n'
                                  f'<code>📅 Праздничные:</code><b> {data["feb_2024"][2]}</b>\n'
                                  f'\n<code>📅 Выходные поверхность:</code><b>4, 5, 11, 12, 18, 19, 23, 24, 25, 26</b>\n'
                                  f'\n<code>🔨 Выходов для 6 часовых:</code><b> {data["feb_2024"][1]}</b>\n'
                                  f'<code>🔨 Выходов для 8 часовых:</code><b> {data["feb_2024"][1]}</b>\n'
                                  f'<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n'
                                  f'<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n'
                                  f'\nНажмите /start, чтобы вернуться в начало', parse_mode="HTML", reply_markup=markup)
    await state.clear()


@router.callback_query(F.data == "mar_days_off_2024")
async def days_off_process_callback_monthh_2024(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Марте 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)

    with codecs.open('settings/days_off_2024.json', 'rb') as f:
        data = json.load(f)
        logger.info(data)

    norm_working_hours, norm_hours_12h_shift, norm_hours_24h_shift = counting_working_days(data["mar_2024"][1])
    markup = keyboard_go_back()  # Клавиатура возврата в начальное меню
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f'<code>✅ Норма выходов в {mar}:</code><b> {data["mar_2024"][1]}</b>\n'
                                  f'<code>✅ Норма времени в {mar}:</code><b> {norm_working_hours}</b>\n'
                                  f'\n<code>📅 Выходные:</code><b>4, 5, 11, 12, 18, 19, 25, 26</b>\n'
                                  f'<code>📅 Праздничные:</code><b> 8</b>\n'
                                  f'\n<code>📅 Выходные поверхность:</code><b>4, 5, 8, 11, 12, 18, 19, 25, 26</b>\n'
                                  f'<code>📅 Выходные подземные:</code><b>1, 5, 8, 12, 15, 19, 22, 26, 29</b>\n'
                                  f'\n<code>🔨 Выходов для 6 часовых:</code><b> {data["mar_2024"][1]}</b>\n'
                                  f'<code>🔨 Выходов для 8 часовых:</code><b> {data["mar_2024"][1]}</b>\n'
                                  f'<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n'
                                  f'<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n'
                                  f'\nНажмите /start, чтобы вернуться в начало', parse_mode="HTML", reply_markup=markup)
    await state.clear()


@router.callback_query(F.data == "apr_days_off_2024")
async def days_off_process_callback_monthh_2024(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Апреле 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)

    with codecs.open('settings/days_off_2024.json', 'rb') as f:
        data = json.load(f)
        logger.info(data)

    norm_working_hours, norm_hours_12h_shift, norm_hours_24h_shift = counting_working_days(data["apr_2024"][1])
    markup = keyboard_go_back()  # Клавиатура возврата в начальное меню
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f'<code>✅ Норма выходов в {apr}:</code><b> {data["apr_2024"][1]}</b>\n'
                                  f'<code>✅ Норма времени в {apr}:</code><b> {norm_working_hours}</b>\n'
                                  f'\n<code>📅 Выходные:</code><b>1, 2, 8, 9, 15, 16, 17, 22, 23, 29, 30</b>\n'
                                  f'<code>📅 Праздничные:</code><b>{data["apr_2024"][2]}</b>\n'
                                  f'\n<code>📅 Выходные поверхность:</code><b>1, 2, 8, 9, 15, 16, 17, 22, 23, 29, 30</b>\n'
                                  f'<code>📅 Выходные подземные:</code><b>1, 2, 5, 9, 12, 16, 17, 19, 23, 26, 30</b>\n'
                                  f'\n<code>🔨 Выходов для 6 часовых:</code><b> {data["apr_2024"][1]}</b>\n'
                                  f'<code>🔨 Выходов для 8 часовых:</code><b> {data["apr_2024"][1]}</b>\n'
                                  f'<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n'
                                  f'<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n'
                                  f'\nНажмите /start, чтобы вернуться в начало', parse_mode="HTML", reply_markup=markup)
    await state.clear()


@router.callback_query(F.data == "may_days_off_2024")
async def days_off_process_callback_monthh_2024(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Мае 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)

    with codecs.open('settings/days_off_2024.json', 'rb') as f:
        data = json.load(f)
        logger.info(data)

    norm_working_hours, norm_hours_12h_shift, norm_hours_24h_shift = counting_working_days(data["may_2024"][1])
    markup = keyboard_go_back()  # Клавиатура возврата в начальное меню
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f'<code>✅ Норма выходов в {may}:</code><b> {data["may_2024"][1]}</b>\n'
                                  f'<code>✅ Норма времени в {may}:</code><b> {norm_working_hours}</b>\n'
                                  f'<code>📅 Праздничные:</code><b> {data["may_2024"][2]}</b>\n'
                                  f'\n<code>📅 Выходные поверхность:</code><b> 1, 4, 5, 6, 9, 10, 11, 12, 13, 18, 19, 25, 26</b>\n'
                                  f'\n<code>📅 Выходные подземные:</code><b> 1, 5, 7, 9, 11, 12, 15, 17, 19, 22, 24, 26, 29</b>\n'
                                  f'\n<code>🔨 Выходов для 6 часовых:</code><b> {data["may_2024"][1]}</b>\n'
                                  f'<code>🔨 Выходов для 8 часовых:</code><b> {data["may_2024"][1]}</b>\n'
                                  f'<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n'
                                  f'<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n'
                                  f'\nНажмите /start, чтобы вернуться в начало', parse_mode="HTML", reply_markup=markup)
    await state.clear()


@router.callback_query(F.data == "june_days_off_2024")
async def days_off_process_callback_monthh_2024(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Июне 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)

    with codecs.open('settings/days_off_2024.json', 'rb') as f:
        data = json.load(f)
        logger.info(data)

    norm_working_hours, norm_hours_12h_shift, norm_hours_24h_shift = counting_working_days(data["june_2024"][1])
    markup = keyboard_go_back()  # Клавиатура возврата в начальное меню
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f'<code>✅ Норма выходов в {june}:</code><b> {data["june_2024"][1]}</b>\n'
                                  f'<code>✅ Норма времени в {june}:</code><b> {norm_working_hours}</b>\n'
                                  f'<code>📅 Праздничные:</code><b> {data["june_2024"][2]}</b>\n'
                                  f'<code>📅 Выходные:</code><b>1, 2, 8, 9, 15, 16, 22, 23, 29, 30</b>\n'
                                  f'\n<code>🔨 Выходов для 6 часовых:</code><b> {data["june_2024"][1]}</b>\n'
                                  f'<code>🔨 Выходов для 8 часовых:</code><b> {data["june_2024"][1]}</b>\n'
                                  f'<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n'
                                  f'<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n'
                                  f'\nНажмите /start, чтобы вернуться в начало', parse_mode="HTML", reply_markup=markup)
    await state.clear()


@router.callback_query(F.data == "jul_days_off_2024")
async def days_off_process_callback_monthh_2024(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Июле 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)

    with codecs.open('settings/days_off_2024.json', 'rb') as f:
        data = json.load(f)
        logger.info(data)

    norm_working_hours, norm_hours_12h_shift, norm_hours_24h_shift = counting_working_days(data["jul_2024"][1])
    markup = keyboard_go_back()  # Клавиатура возврата в начальное меню
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f'<code>✅ Норма выходов в {jul}:</code><b> {data["jul_2024"][1]}</b>\n'
                                  f'<code>✅ Норма времени в {jul}:</code><b> {norm_working_hours}</b>\n'
                                  f'<code>📅 Праздничные:</code><b> {data["jul_2024"][2]}</b>\n'
                                  f'\n<code>📅 Выходные:</code><b>6, 7, 13, 14, 20, 21, 27, 28</b>\n'
                                  f'\n<code>🔨 Выходов для 6 часовых:</code><b> {data["jul_2024"][1]}</b>\n'
                                  f'<code>🔨 Выходов для 8 часовых:</code><b> {data["jul_2024"][1]}</b>\n'
                                  f'<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n'
                                  f'<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n'
                                  f'\nНажмите /start, чтобы вернуться в начало', parse_mode="HTML", reply_markup=markup)
    await state.clear()


@router.callback_query(F.data == "aug_days_off_2024")
async def days_off_process_callback_monthh_2024(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Августе 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)

    with codecs.open('settings/days_off_2024.json', 'rb') as f:
        data = json.load(f)
        logger.info(data)

    norm_working_hours, norm_hours_12h_shift, norm_hours_24h_shift = counting_working_days(data["aug_2024"][1])
    markup = keyboard_go_back()  # Клавиатура возврата в начальное меню
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f'<code>✅ Норма выходов в {aug}:</code><b> {data["aug_2024"][1]}</b>\n'
                                  f'<code>✅ Норма времени в {aug}:</code><b> {norm_working_hours}</b>\n'
                                  f'<code>📅 Праздничные:</code><b> {data["aug_2024"][2]}</b>\n'
                                  f'\n<code>📅 Выходные:</code><b>3, 4, 10, 11, 17, 18, 24, 25, 31</b>\n'
                                  f'\n<code>🔨 Выходов для 6 часовых:</code><b> {data["aug_2024"][1]}</b>\n'
                                  f'<code>🔨 Выходов для 8 часовых:</code><b> {data["aug_2024"][1]}</b>\n'
                                  f'<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n'
                                  f'<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n'
                                  f'\nНажмите /start, чтобы вернуться в начало', parse_mode="HTML", reply_markup=markup)
    await state.clear()


@router.callback_query(F.data == "sep_days_off_2024")
async def days_off_process_callback_monthh_2024(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Сентябре 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)

    with codecs.open('settings/days_off_2024.json', 'rb') as f:
        data = json.load(f)
        logger.info(data)

    norm_working_hours, norm_hours_12h_shift, norm_hours_24h_shift = counting_working_days(data["sep_2024"][1])
    markup = keyboard_go_back()  # Клавиатура возврата в начальное меню
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f'<code>✅ Норма выходов в {sep}:</code><b> {data["sep_2024"][1]}</b>\n'
                                  f'<code>✅ Норма времени в {sep}:</code><b> {norm_working_hours}</b>\n'
                                  f'<code>📅 Праздничные:</code><b> {data["sep_2024"][2]}</b>\n'
                                  f'\n<code>📅 Выходные:</code><b> 1, 7, 8, 14, 15, 21, 22, 28, 29</b>\n'
                                  f'\n<code>🔨 Выходов для 6 часовых:</code><b> {data["sep_2024"][1]}</b>\n'
                                  f'<code>🔨 Выходов для 8 часовых:</code><b> {data["sep_2024"][1]}</b>\n'
                                  f'<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n'
                                  f'<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n'
                                  f'\nНажмите /start, чтобы вернуться в начало', parse_mode="HTML", reply_markup=markup)
    await state.clear()


@router.callback_query(F.data == "oct_days_off_2024")
async def days_off_process_callback_monthh_2024(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Октябре 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)

    with codecs.open('settings/days_off_2024.json', 'rb') as f:
        data = json.load(f)
        logger.info(data)

    norm_working_hours, norm_hours_12h_shift, norm_hours_24h_shift = counting_working_days(data["oct_2024"][1])
    markup = keyboard_go_back()  # Клавиатура возврата в начальное меню
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f'<code>✅ Норма выходов в {oct}:</code><b> {data["oct_2024"][1]}</b>\n'
                                  f'<code>✅ Норма времени в {oct}:</code><b> {norm_working_hours}</b>\n'
                                  f'<code>📅 Праздничные:</code><b> {data["oct_2024"][2]}</b>\n'
                                  f'<code>📅 Выходные:</code><b>5, 6, 12, 13, 19, 20, 26, 27</b>\n'
                                  f'\n<code>🔨 Выходов для 6 часовых:</code><b> {data["oct_2024"][1]}</b>\n'
                                  f'<code>🔨 Выходов для 8 часовых:</code><b> {data["oct_2024"][1]}</b>\n'
                                  f'<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n'
                                  f'<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n'
                                  f'\nНажмите /start, чтобы вернуться в начало', parse_mode="HTML", reply_markup=markup)
    await state.clear()


@router.callback_query(F.data == "nov_days_off_2024")
async def days_off_process_callback_monthh_2024(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Ноябре 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)

    with codecs.open('settings/days_off_2024.json', 'rb') as f:
        data = json.load(f)
        logger.info(data)

    norm_working_hours, norm_hours_12h_shift, norm_hours_24h_shift = counting_working_days(data["nov_2024"][1])
    markup = keyboard_go_back()  # Клавиатура возврата в начальное меню
    # добавляем разметку в сообщение
    response_message = callback_query.message
    await response_message.answer(f'<code>✅ Норма выходов в {nov}:</code><b> {data["nov_2024"][1]}</b>\n'
                                  f'<code>✅ Норма времени в {nov}:</code><b> {norm_working_hours}</b>\n'
                                  f'<code>📅 Праздничные:</code><b> {data["nov_2024"][2]}</b>\n'
                                  f'\n<code>📅 Выходные:</code><b>3, 9, 10, 16, 17, 23, 24, 30</b>\n'
                                  f'\n<code>🔨 Выходов для 6 часовых:</code><b> {data["nov_2024"][1]}</b>\n'
                                  f'<code>🔨 Выходов для 8 часовых:</code><b> {data["nov_2024"][1]}</b>\n'
                                  f'<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n'
                                  f'<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n'
                                  f'\nНажмите /start, чтобы вернуться в начало', parse_mode="HTML", reply_markup=markup)
    await state.clear()


@router.callback_query(F.data == "dec_days_off_2024")
async def days_off_process_callback_monthh_2024(callback_query: types.CallbackQuery, state: FSMContext):
    """Выходные дни в Декабре 2023"""
    selected_month = callback_query.data
    await state.update_data(month=selected_month)

    with codecs.open('settings/days_off_2024.json', 'rb') as f:
        data = json.load(f)
        logger.info(data)

    norm_working_hours, norm_hours_12h_shift, norm_hours_24h_shift = counting_working_days(data["dec_2024"][1])
    markup = keyboard_go_back()  # Клавиатура возврата в начальное меню

    text_message = (f'<code>✅ Норма выходов в {dec}:</code><b> {data["dec_2024"][1]}</b>\n'
                    f'<code>✅ Норма времени в {dec}:</code><b> {norm_working_hours}</b>\n'
                    f'<code>📅 Праздничные:</code><b> {data["dec_2024"][2]}</b>\n'
                    f'\n<code>📅 Выходные дни:</code><b> 1, 7, 8, 14, 15, 21, 22, 29, 30, 31</b>\n'
                    f'\n<code>🔨 Выходов для 6 часовых:</code><b> {data["dec_2024"][1]}</b>\n'
                    f'<code>🔨 Выходов для 8 часовых:</code><b> {data["dec_2024"][1]}</b>\n'
                    f'<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n'
                    f'<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n'
                    f'\nНажмите /start, чтобы вернуться в начало')

    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text=text_message,
        parse_mode="HTML",
        reply_markup=markup
    )
    await state.clear()


def register_days_off_callback_month_handler_2024():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(days_off_callback_month_2024)
