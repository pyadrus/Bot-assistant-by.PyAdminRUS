# -*- coding: utf-8 -*-
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loguru import logger

from system.global_variables import (jan, mar, apr, may, june, jul, aug, sep, oct_23, nov, dec, feb, jan_2024, feb_2024,
                                     mar_2024, apr_2024, may_2024, june_2024, jul_2024, aug_2024, sep_2024, oct_2024,
                                     nov_2024, dec_2024, jan_22, feb_22, mar_22, apr_22, may_22, june_22, jul_22,
                                     aug_22, sep_22, oct_22, nov_22, dec_22, jan_2025, feb_2025, mar_2025, apr_2025,
                                     may_2025, june_2025, jul_2025, aug_2025, sep_2025, oct_2025, nov_2025, dec_2025)


def welcome_keyboard():
    """Клавиатура приветствия выбора: рапортов, работы в выходной день, обратная связь с пользователем"""
    try:
        rows = [
            [InlineKeyboardButton(text='🔨Рапорта 2023', callback_data='rap'),
             InlineKeyboardButton(text='🔨Рапорта 2024', callback_data='rap_2024')],

            [InlineKeyboardButton(text="🔨Рапорта 2025", callback_data="rap_2025")],

            [InlineKeyboardButton(text="📈 Табеля", callback_data="table")],

            [InlineKeyboardButton(text='📅 Выходные дни 2022', callback_data='days_off_22'),
             InlineKeyboardButton(text='📅 Выходные дни 2023', callback_data='days_off')],

            [InlineKeyboardButton(text='📅 Выходные дни 2024', callback_data='days_off_24')],
            [InlineKeyboardButton(text='📅 Выходные дни 2025', callback_data='days_off_25')],

            [InlineKeyboardButton(text='🗂 Образцы приказов', callback_data='sample_orders'),
             InlineKeyboardButton(text='Бланк лимитки М-8', callback_data='limit_form')],

            [InlineKeyboardButton(text='Образец договор', callback_data='contract_form')],
            [InlineKeyboardButton(text='⁉️ Напомнить, замечание', callback_data='feedback')],
        ]
        main_keyboard = InlineKeyboardMarkup(inline_keyboard=rows)
        return main_keyboard
    except Exception as e:
        logger.exception(e)


def keyboard_for_report_2023():
    """Клавиатура для рапорта 2023"""
    try:
        rows = [
            [InlineKeyboardButton(text=f'✅ {jan}', callback_data='01_jan_rap'),
             InlineKeyboardButton(text=f'✅ {feb}', callback_data='02_feb_rap'),
             InlineKeyboardButton(text=f'✅ {mar}', callback_data='03_mar_rap')],

            [InlineKeyboardButton(text=f'✅ {apr}', callback_data='04_apr_rap'),
             InlineKeyboardButton(text=f'✅ {may}', callback_data='05_may_rap'),
             InlineKeyboardButton(text=f'✅ {june}', callback_data='06_jun_rap')],

            [InlineKeyboardButton(text=f'✅ {jul}', callback_data='07_jul_rap'),
             InlineKeyboardButton(text=f'✅ {aug}', callback_data='08_aug_rap'),
             InlineKeyboardButton(text=f'✅ {sep}', callback_data='09_sep_rap')],

            [InlineKeyboardButton(text=f'✅ {oct_23}', callback_data='10_oct_rap'),
             InlineKeyboardButton(text=f'✅ {nov}', callback_data='11_nov_rap'),
             InlineKeyboardButton(text=f'✅ {dec}', callback_data='12_dec_rap')],

            [InlineKeyboardButton(text='↩️  Вернуться в начальное меню', callback_data='menu')],
        ]
        main_keyboard = InlineKeyboardMarkup(inline_keyboard=rows)
        return main_keyboard
    except Exception as e:
        logger.exception(e)


def keyboard_for_report_2025():
    """Клавиатура для рапорта 2025"""
    try:
        rows = [
            [InlineKeyboardButton(text=f'✅ {jan_2025}', callback_data='01_jan_rap_2025'),
             InlineKeyboardButton(text=f'{feb_2025}', callback_data='02_feb_rap_2025'),
             InlineKeyboardButton(text=f'{mar_2025}', callback_data='03_mar_rap_2025')],

            [InlineKeyboardButton(text=f'{apr_2025}', callback_data='04_apr_rap_2025'),
             InlineKeyboardButton(text=f'{may_2025}', callback_data='05_may_rap_2025'),
             InlineKeyboardButton(text=f'{june_2025}', callback_data='06_jun_rap_2025')],

            [InlineKeyboardButton(text=f'{jul_2025}', callback_data='07_jul_rap_2025'),
             InlineKeyboardButton(text=f'{aug_2025}', callback_data='08_aug_rap_2025'),
             InlineKeyboardButton(text=f'{sep_2025}', callback_data='09_sep_rap_2025')],

            [InlineKeyboardButton(text=f'{oct_2025}', callback_data='10_oct_rap_2025'),
             InlineKeyboardButton(text=f'{nov_2025}', callback_data='11_nov_rap_2025'),
             InlineKeyboardButton(text=f'{dec_2025}', callback_data='12_dec_rap_2025')],

            [InlineKeyboardButton(text='↩️  Вернуться в начальное меню', callback_data='menu')],
        ]
        main_keyboard = InlineKeyboardMarkup(inline_keyboard=rows)
        return main_keyboard
    except Exception as e:
        logger.exception(e)


def keyboard_for_report_2024():
    """Клавиатура для рапорта 2024"""
    try:
        rows = [
            [InlineKeyboardButton(text=f'✅ {jan_2024}', callback_data='01_jan_rap_2024'),
             InlineKeyboardButton(text=f'✅ {feb_2024}', callback_data='02_feb_rap_2024'),
             InlineKeyboardButton(text=f'✅ {mar_2024}', callback_data='03_mar_rap_2024')],

            [InlineKeyboardButton(text=f'✅ {apr_2024}', callback_data='04_apr_rap_2024'),
             InlineKeyboardButton(text=f'✅ {may_2024}', callback_data='05_may_rap_2024'),
             InlineKeyboardButton(text=f'✅ {june_2024}', callback_data='06_jun_rap_2024')],

            [InlineKeyboardButton(text=f'✅ {jul_2024}', callback_data='07_jul_rap_2024'),
             InlineKeyboardButton(text=f'✅ {aug_2024}', callback_data='08_aug_rap_2024'),
             InlineKeyboardButton(text=f'✅ {sep_2024}', callback_data='09_sep_rap_2024')],

            [InlineKeyboardButton(text=f'✅ {oct_2024}', callback_data='10_oct_rap_2024'),
             InlineKeyboardButton(text=f'✅ {nov_2024}', callback_data='11_nov_rap_2024'),
             InlineKeyboardButton(text=f'✅ {dec_2024}', callback_data='12_dec_rap_2024')],

            [InlineKeyboardButton(text='↩️  Вернуться в начальное меню', callback_data='menu')],
        ]
        main_keyboard = InlineKeyboardMarkup(inline_keyboard=rows)
        return main_keyboard
    except Exception as e:
        logger.exception(e)


def return_start_menu_keyboard():
    """Возврат в начальное меню"""
    try:
        # Создаем клавиатуру с двумя кнопками
        rows = [
            [InlineKeyboardButton(text='🔨Рапорта 2023', callback_data='rap')],
            [InlineKeyboardButton(text='🔨Рапорта 2024', callback_data='rap_2024')],
            [InlineKeyboardButton(text='🔨Рапорта 2025', callback_data='rap_2025')],
            [InlineKeyboardButton(text='↩️  Вернуться в начальное меню', callback_data='menu')],
        ]
        keyboard_return = InlineKeyboardMarkup(inline_keyboard=rows)
        return keyboard_return
    except Exception as e:
        logger.exception(e)


def output_sheet_by_area():
    """Табеля по участкам"""
    try:
        rows = [
            [InlineKeyboardButton(text=f'2021', callback_data='year_21'),
             InlineKeyboardButton(text=f'2022', callback_data='year_22'),
             InlineKeyboardButton(text=f'2023', callback_data='year_23'),
             InlineKeyboardButton(text=f'2024', callback_data='year_24')],

            [InlineKeyboardButton(text='↩️  Вернуться в начальное меню', callback_data='menu')],
        ]
        main_keyboard = InlineKeyboardMarkup(inline_keyboard=rows)
        return main_keyboard
    except Exception as e:
        logger.exception(e)


def work_on_days_off_2022():
    """Работа в выходной день 2022"""
    rows = [
        [InlineKeyboardButton(text=f'✅ {jan_22}', callback_data='jan_days_off_2022'),
         InlineKeyboardButton(text=f'✅ {feb_22}', callback_data='feb_days_off_2022'),
         InlineKeyboardButton(text=f'✅ {mar_22}', callback_data='mar_days_off_2022')],

        [InlineKeyboardButton(text=f'✅ {apr_22}', callback_data='apr_days_off_2022'),
         InlineKeyboardButton(text=f'✅ {may_22}', callback_data='may_days_off_2022'),
         InlineKeyboardButton(text=f'✅ {june_22}', callback_data='june_days_off_2022')],

        [InlineKeyboardButton(text=f'✅ {jul_22}', callback_data='jul_days_off_2022'),
         InlineKeyboardButton(text=f'✅ {aug_22}', callback_data='aug_days_off_2022'),
         InlineKeyboardButton(text=f'✅ {sep_22}', callback_data='sep_days_off_2022')],

        [InlineKeyboardButton(text=f'✅ {oct_22}', callback_data='oct_days_off_2022'),
         InlineKeyboardButton(text=f'✅ {nov_22}', callback_data='nov_days_off_2022'),
         InlineKeyboardButton(text=f'✅ {dec_22}', callback_data='dec_days_off_2022')],

        [InlineKeyboardButton(text=f'🔨 Количество рабочих дней в 2022 году',
                              callback_data='working_days_per_year_2022')],

        [InlineKeyboardButton(text='↩️  Вернуться в начальное меню', callback_data='menu')],
    ]
    main_keyboard = InlineKeyboardMarkup(inline_keyboard=rows)
    return main_keyboard


def work_on_days_off_2023():
    """Работа в выходной день 2023"""
    rows = [
        [InlineKeyboardButton(text=f'✅ {jan}', callback_data='jan_days_off'),
         InlineKeyboardButton(text=f'✅ {feb}', callback_data='feb_days_off'),
         InlineKeyboardButton(text=f'✅ {mar}', callback_data='mar_days_off')],

        [InlineKeyboardButton(text=f'✅ {apr}', callback_data='apr_days_off'),
         InlineKeyboardButton(text=f'✅ {may}', callback_data='may_days_off'),
         InlineKeyboardButton(text=f'✅ {june}', callback_data='june_days_off')],

        [InlineKeyboardButton(text=f'✅ {jul}', callback_data='jul_days_off'),
         InlineKeyboardButton(text=f'✅ {aug}', callback_data='aug_days_off'),
         InlineKeyboardButton(text=f'✅ {sep}', callback_data='sep_days_off')],

        [InlineKeyboardButton(text=f'✅ {oct_23}', callback_data='oct_days_off'),
         InlineKeyboardButton(text=f'✅ {nov}', callback_data='nov_days_off'),
         InlineKeyboardButton(text=f'✅ {dec}', callback_data='dec_days_off')],

        [InlineKeyboardButton(text=f'🔨 Количество рабочих дней в 2023 году',
                              callback_data='working_days_per_year')],

        [InlineKeyboardButton(text='↩️  Вернуться в начальное меню', callback_data='menu')],
    ]
    main_keyboard = InlineKeyboardMarkup(inline_keyboard=rows)
    return main_keyboard


def work_on_days_off_2024(data):
    """Работа в выходной день 2024"""
    rows = [
        [InlineKeyboardButton(text=f' {data["jan_2024"][0]}', callback_data='jan_days_off_2024'),
         InlineKeyboardButton(text=f' {data["feb_2024"][0]}', callback_data='feb_days_off_2024'),
         InlineKeyboardButton(text=f' {data["mar_2024"][0]}', callback_data='mar_days_off_2024')],

        [InlineKeyboardButton(text=f' {data["apr_2024"][0]}', callback_data='apr_days_off_2024'),
         InlineKeyboardButton(text=f' {data["may_2024"][0]}', callback_data='may_days_off_2024'),
         InlineKeyboardButton(text=f' {data["june_2024"][0]}', callback_data='june_days_off_2024')],

        [InlineKeyboardButton(text=f' {data["jul_2024"][0]}', callback_data='jul_days_off_2024'),
         InlineKeyboardButton(text=f' {data["aug_2024"][0]}', callback_data='aug_days_off_2024'),
         InlineKeyboardButton(text=f' {data["sep_2024"][0]}', callback_data='sep_days_off_2024')],

        [InlineKeyboardButton(text=f'{data["oct_2024"][0]}', callback_data='oct_days_off_2024'),
         InlineKeyboardButton(text=f'{data["nov_2024"][0]}', callback_data='nov_days_off_2024'),
         InlineKeyboardButton(text=f'{data["dec_2024"][0]}', callback_data='dec_days_off_2024')],

        [InlineKeyboardButton(text=f'🔨 Количество рабочих дней в 2024 году',
                              callback_data='working_days_per_year_2024')],

        [InlineKeyboardButton(text='↩️  Вернуться в начальное меню', callback_data='menu')],
    ]
    main_keyboard = InlineKeyboardMarkup(inline_keyboard=rows)
    return main_keyboard

def work_on_days_off_2025(data):
    """Работа в выходной день 2025"""
    rows = [
        [InlineKeyboardButton(text=f' {data["jan_2025"][0]}', callback_data='jan_days_off_2025'),
         InlineKeyboardButton(text=f' {data["feb_2025"][0]}', callback_data='feb_days_off_2025'),
         InlineKeyboardButton(text=f' {data["mar_2025"][0]}', callback_data='mar_days_off_2025')],

        [InlineKeyboardButton(text=f' {data["apr_2025"][0]}', callback_data='apr_days_off_2025'),
         InlineKeyboardButton(text=f' {data["may_2025"][0]}', callback_data='may_days_off_2025'),
         InlineKeyboardButton(text=f' {data["june_2025"][0]}', callback_data='june_days_off_2025')],

        [InlineKeyboardButton(text=f' {data["jul_2025"][0]}', callback_data='jul_days_off_2025'),
         InlineKeyboardButton(text=f' {data["aug_2025"][0]}', callback_data='aug_days_off_2025'),
         InlineKeyboardButton(text=f' {data["sep_2025"][0]}', callback_data='sep_days_off_2025')],

        [InlineKeyboardButton(text=f'{data["oct_2025"][0]}', callback_data='oct_days_off_2025'),
         InlineKeyboardButton(text=f'{data["nov_2025"][0]}', callback_data='nov_days_off_2025'),
         InlineKeyboardButton(text=f'{data["dec_2025"][0]}', callback_data='dec_days_off_2025')],

        [InlineKeyboardButton(text=f'🔨 Количество рабочих дней в 2025 году',
                              callback_data='working_days_per_year_2025')],

        [InlineKeyboardButton(text='↩️  Вернуться в начальное меню', callback_data='menu')],
    ]
    main_keyboard = InlineKeyboardMarkup(inline_keyboard=rows)
    return main_keyboard

def sample_orders_keyboard():
    """Клавиатура с примерными образцами приказов"""
    # Создаем клавиатуру с двумя кнопками
    rows = [
        [InlineKeyboardButton(text=f'Оплата за праздничный день',
                              callback_data='payment_on_public_holidays')],
        [InlineKeyboardButton(text=f'Выходной за праздничный день',
                              callback_data='day_off_for_public_holiday')],
        [InlineKeyboardButton(text='↩️  Вернуться в начальное меню', callback_data='menu')],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=rows)
    return keyboard


def create_feedback_and_return_to_menu_keyboard():
    # Создаем клавиатуру с двумя кнопками
    # Создаем клавиатуру с двумя кнопками
    rows = [
        [InlineKeyboardButton(text='⁉️ Если рапорт не найден, нажмите ТУТ', callback_data='feedback')],
        [InlineKeyboardButton(text='↩️  Вернуться в начальное меню', callback_data='menu')],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=rows)
    return keyboard


def keyboard_go_back() -> InlineKeyboardMarkup:
    """Клавиатура '↩️ Вернуться в начальное меню'"""
    try:
        # Создаем клавиатуру с двумя кнопками
        rows = [
            [InlineKeyboardButton(text='↩️  Вернуться в начальное меню', callback_data='menu')]
        ]
        keyboard = InlineKeyboardMarkup(inline_keyboard=rows)
        return keyboard

    except Exception as e:
        logger.exception(e)


if __name__ == "__main__":
    welcome_keyboard()
    keyboard_go_back()
    keyboard_for_report_2023()
    keyboard_for_report_2024()
    output_sheet_by_area()
    work_on_days_off_2022()
    work_on_days_off_2023()
    sample_orders_keyboard()
