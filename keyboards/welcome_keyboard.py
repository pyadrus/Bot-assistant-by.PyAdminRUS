from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def welcome_keyboard():
    """Клавиатура приветствия выбора: рапортов, работы в выходной день, обратная связь с пользователем"""
    main_keyboard = InlineKeyboardMarkup()
    raport_button = InlineKeyboardButton(text='🔨Рапорта 2023', callback_data='rap')
    raport_button_2024 = InlineKeyboardButton(text='🔨Рапорта 2024', callback_data='rap_2024')
    table_button = InlineKeyboardButton(text="📈 Табеля", callback_data="table")
    days_off_button_22 = InlineKeyboardButton(text='📅 Выходные дни 2022', callback_data='days_off_22')
    days_off_button_23 = InlineKeyboardButton(text='📅 Выходные дни 2023', callback_data='days_off')
    days_off_button_24 = InlineKeyboardButton(text='📅 Выходные дни 2024', callback_data='days_off_24')
    sample_orders = InlineKeyboardButton(text='🗂 Образцы приказов', callback_data='sample_orders')
    feedback_button = InlineKeyboardButton(text='⁉️ Напомнить, замечание', callback_data='feedback')
    # feedback_ai_button = InlineKeyboardButton(text='⁉️ Задать вопрос ИИ', callback_data='feedback_ai')
    main_keyboard.row(raport_button, raport_button_2024)
    main_keyboard.row(table_button)
    main_keyboard.row(days_off_button_22, days_off_button_23)
    main_keyboard.row(days_off_button_24)
    main_keyboard.row(sample_orders)
    main_keyboard.row(feedback_button)
    return main_keyboard


def return_start_menu_keyboard():
    """Возврат в начальное меню"""
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


def keyboard_go_back() -> InlineKeyboardMarkup:
    """Клавиатура '↩️ Вернуться в начальное меню'"""
    markup = InlineKeyboardMarkup()  # создаем клавиатуру
    return_to_menu_button = InlineKeyboardButton(text='↩️  Вернуться в начальное меню', callback_data='menu')
    # создаем разметку для кнопки
    markup.add(return_to_menu_button)
    return markup


if __name__ == "__main__":
    welcome_keyboard()
    keyboard_go_back()
