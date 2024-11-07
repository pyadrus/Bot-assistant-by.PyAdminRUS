from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def welcome_keyboard_admin():
    """Клавиатура приветствия админа"""

    rows = [
        [InlineKeyboardButton(text='Зарегистрированные пользователи', callback_data='registered_users')],
         [InlineKeyboardButton(text="Активные пользователи", callback_data="active_users")],
         [InlineKeyboardButton(text='Коллективный договор', callback_data='collective_agreement')],

        [ InlineKeyboardButton(text='Список участков', callback_data='list_of_sites')],
        [ InlineKeyboardButton(text='Проверка наличия рапортов', callback_data='checking_availability_of_reports')],
        [ InlineKeyboardButton(text='Переименование рапортов', callback_data='renaming_reports')],

        [ InlineKeyboardButton(text='↩️  Вернуться в начальное меню', callback_data='menu')],
    ]

    main_keyboard = InlineKeyboardMarkup(inline_keyboard=rows)
    return main_keyboard


if __name__ == '__main__':
    welcome_keyboard_admin()  # Клавиатура приветствие админа
