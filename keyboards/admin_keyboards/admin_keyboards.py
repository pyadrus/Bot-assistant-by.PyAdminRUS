# -*- coding: utf-8 -*-
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def welcome_keyboard_admin():
    """Клавиатура приветствия админа"""

    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Зарегистрированные пользователи', callback_data='registered_users')],
        [InlineKeyboardButton(text="Активные пользователи", callback_data="active_users")],
        [InlineKeyboardButton(text='Коллективный договор', callback_data='collective_agreement')],

        [InlineKeyboardButton(text='Список участков', callback_data='list_of_sites')],
        [InlineKeyboardButton(text='Проверка наличия рапортов', callback_data='checking_availability_of_reports')],
        [InlineKeyboardButton(text='Проверка наличия табеля 2024', callback_data='checking_availability_of_tab')],
        [InlineKeyboardButton(text='Переименование рапортов', callback_data='renaming_reports')],

        [InlineKeyboardButton(text='↩️  Вернуться в начальное меню', callback_data='menu')],
    ])


if __name__ == '__main__':
    welcome_keyboard_admin()  # Клавиатура приветствие админа
