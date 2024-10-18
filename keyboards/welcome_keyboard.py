from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loguru import logger


def welcome_keyboard():
    """Клавиатура приветствия выбора: рапортов, работы в выходной день, обратная связь с пользователем"""
    try:

        rows = [
            [InlineKeyboardButton(text='🔨Рапорта 2023', callback_data='rap'),
             InlineKeyboardButton(text='🔨Рапорта 2024', callback_data='rap_2024')],
            [InlineKeyboardButton(text="📈 Табеля", callback_data="table")],
            [InlineKeyboardButton(text='📅 Выходные дни 2022', callback_data='days_off_22'),
             InlineKeyboardButton(text='📅 Выходные дни 2023', callback_data='days_off')],
            [InlineKeyboardButton(text='📅 Выходные дни 2024', callback_data='days_off_24')],
            [InlineKeyboardButton(text='🗂 Образцы приказов', callback_data='sample_orders'),
             InlineKeyboardButton(text='Бланк лимитки М-8', callback_data='limit_form')],
            [InlineKeyboardButton(text='Образец договор', callback_data='contract_form')],
            [InlineKeyboardButton(text='⁉️ Напомнить, замечание', callback_data='feedback')],
        ]
        main_keyboard = InlineKeyboardMarkup(inline_keyboard=rows)
        return main_keyboard

    except Exception as e:
        logger.exception(e)


def return_start_menu_keyboard():
    """Возврат в начальное меню"""
    try:
        # Создаем клавиатуру с двумя кнопками
        keyboard_return = InlineKeyboardMarkup()
        raport_button_2023 = InlineKeyboardButton(text='🔨Рапорта 2023', callback_data='rap')
        raport_button_2024 = InlineKeyboardButton(text='🔨Рапорта 2024', callback_data='rap_2024')
        return_to_menu_button = InlineKeyboardButton(text='↩️  Вернуться в начальное меню', callback_data='menu')

        # Добавляем кнопки к клавиатуре
        keyboard_return.add(return_to_menu_button)
        keyboard_return.add(raport_button_2023)
        keyboard_return.add(raport_button_2024)

        return keyboard_return
    except Exception as e:
        logger.exception(e)


def keyboard_go_back() -> InlineKeyboardMarkup:
    """Клавиатура '↩️ Вернуться в начальное меню'"""
    try:
        markup = InlineKeyboardMarkup()  # создаем клавиатуру
        return_to_menu_button = InlineKeyboardButton(text='↩️  Вернуться в начальное меню', callback_data='menu')
        # создаем разметку для кнопки
        markup.add(return_to_menu_button)
        return markup
    except Exception as e:
        logger.exception(e)


if __name__ == "__main__":
    welcome_keyboard()
    keyboard_go_back()
