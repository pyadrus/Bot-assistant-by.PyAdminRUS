# -*- coding: utf-8 -*-
from aiogram import types, F

from keyboards.welcome_keyboard import output_sheet_by_area
from system.system import dp, bot, router


@router.callback_query(F.data == "table")
async def table_handler(callback_query: types.CallbackQuery):
    """Табель выходов с 2021 по 2024"""
    await bot.send_message(callback_query.from_user.id, "📅 Выберите год:", reply_markup=output_sheet_by_area())


@router.callback_query(F.data == "year_21")
async def table_handler_21(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "📅 год 2021:")


@router.callback_query(F.data == "year_22")
async def table_handler_22(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "📅 год 2022:")


@router.callback_query(F.data == "year_23")
async def table_handler_23(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "📅 год 2023:")


@router.callback_query(F.data == "year_24")
async def table_handler_24(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "📅 год 2024:")


def register_table_handler_handler():
    """Регистрируем handlers для работы в выходной день"""
    dp.register_message_handler(table_handler)
    dp.register_message_handler(table_handler_21)
    dp.register_message_handler(table_handler_22)
    dp.register_message_handler(table_handler_23)
    dp.register_message_handler(table_handler_24)
