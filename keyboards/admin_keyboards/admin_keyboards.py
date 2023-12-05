from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def welcome_keyboard_admin():
    """Клавиатура приветствия админа"""
    main_keyboard = InlineKeyboardMarkup()
    registered_users_button = InlineKeyboardButton(text='Зарегистрированные пользователи', callback_data='registered_users')
    active_users_button = InlineKeyboardButton(text="Активные пользователи", callback_data="active_users")
    collective_agreement_button = InlineKeyboardButton(text='Коллективный договор', callback_data='collective_agreement')
    list_of_sites_button = InlineKeyboardButton(text='Список участков', callback_data='list_of_sites')
    checking_availability_of_reports_button = InlineKeyboardButton(text='Проверка наличия рапортов', callback_data='checking_availability_of_reports')
    renaming_reports_button = InlineKeyboardButton(text='Переименование рапортов', callback_data='renaming_reports')
    main_keyboard.row(registered_users_button)
    main_keyboard.row(active_users_button)
    main_keyboard.row(collective_agreement_button)
    main_keyboard.row(list_of_sites_button)
    main_keyboard.row(checking_availability_of_reports_button)
    main_keyboard.row(renaming_reports_button)
    return main_keyboard


if __name__ == '__main__':
    welcome_keyboard_admin() # Клавиатура приветствие админа