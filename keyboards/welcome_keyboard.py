from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def welcome_keyboard():
    """Клавиатура приветствия выбора: рапортов, работы в выходной день, обратная связь с пользователем"""
    main_keyboard = InlineKeyboardMarkup()
    raport_button = InlineKeyboardButton(text='🔨Рапорта 2023', callback_data='rap')
    days_off_button_22 = InlineKeyboardButton(text='📅 Выходные дни 2022', callback_data='days_off_22')
    days_off_button_23 = InlineKeyboardButton(text='📅 Выходные дни 2023', callback_data='days_off')
    feedback_button = InlineKeyboardButton(text='⁉️ Задать вопрос, напомнить, замечание', callback_data='feedback')
    main_keyboard.row(raport_button)
    main_keyboard.row(days_off_button_22, days_off_button_23)
    main_keyboard.row(feedback_button)
    return main_keyboard


if __name__ == "__main__":
    welcome_keyboard()
