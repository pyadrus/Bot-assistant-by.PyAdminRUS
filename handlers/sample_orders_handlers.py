import datetime
import os

from aiogram import types, F
from aiogram.fsm.context import FSMContext
from loguru import logger
from aiogram.types import FSInputFile
from database.database import perform_database_operations
from keyboards.welcome_keyboard import keyboard_go_back, sample_orders_keyboard
from system.system import dp, bot, router


@router.callback_query(F.data == "sample_orders")
async def sample_orders(callback_query: types.CallbackQuery):
    """Кнопки с месяцами рапорта"""
    await bot.send_message(callback_query.from_user.id, "Выберите приказ:", reply_markup=sample_orders_keyboard())


@router.callback_query(F.data == "contract_form")
async def contract_form(callback_query: types.CallbackQuery, state: FSMContext):
    """Образец приказа оплата в праздничные дни"""
    try:
        user_id = callback_query.from_user.id
        username = callback_query.from_user.username
        timestamp = datetime.datetime.now()
        file_name = 'Шаблон трудовой договор.docx'
        perform_database_operations(user_id, username, timestamp, file_name)
        logger.info(f'Пользователь: username {username}, ID {user_id}, запросил файл {file_name} в {timestamp}')
        # Поиск и отправка файла
        file_path = f"raports/sample_orders/{file_name}"
        if os.path.isfile(file_path):

            file = FSInputFile(file_path)
            await bot.send_document(
                callback_query.from_user.id,
                document=file,
                caption=f"{file_name}",
            )

    except Exception as e:
        logger.error(f"An error occurred: {e}")

    await state.clear()


@router.callback_query(F.data == "limit_form")
async def limit_form(callback_query: types.CallbackQuery, state: FSMContext):
    """Образец приказа оплата в праздничные дни"""
    try:
        user_id = callback_query.from_user.id
        username = callback_query.from_user.username
        timestamp = datetime.datetime.now()
        file_name = 'Бланк лимитки М-8.docx'
        perform_database_operations(user_id, username, timestamp, file_name)
        logger.info(f'Пользователь: username {username}, ID {user_id}, запросил файл {file_name} в {timestamp}')
        # Поиск и отправка файла
        file_path = f"raports/sample_orders/{file_name}"
        if os.path.isfile(file_path):
            keyboard_return = keyboard_go_back()
            file = FSInputFile(file_path)
            await bot.send_document(callback_query.from_user.id, document=file,
                                    caption=f"Бланк лимитки М-8", reply_markup=keyboard_return)
    except Exception as e:
        logger.error(f"An error occurred: {e}")

    await state.clear()


@router.callback_query(F.data == "payment_on_public_holidays")
async def payment_on_public_holidays(callback_query: types.CallbackQuery, state: FSMContext):
    """Образец приказа оплата в праздничные дни"""
    try:
        user_id = callback_query.from_user.id
        username = callback_query.from_user.username
        timestamp = datetime.datetime.now()
        file_name = 'Оплата праздничные дни.doc'
        perform_database_operations(user_id, username, timestamp, file_name)

        # Поиск и отправка файла
        file_path = "raports/sample_orders/Оплата праздничные дни.doc"
        if os.path.isfile(file_path):
            file = FSInputFile(file_path)
            keyboard_return = keyboard_go_back()
            await bot.send_document(callback_query.from_user.id, document=file,
                                    caption=f"Образец приказа: {file_name}", reply_markup=keyboard_return)
    except Exception as e:
        logger.error(f"An error occurred: {e}")

    await state.clear()


@router.callback_query(F.data == "day_off_for_public_holiday")
async def day_off_for_public_holiday(callback_query: types.CallbackQuery, state: FSMContext):
    """Образец приказа выходной за праздничный день"""
    try:
        user_id = callback_query.from_user.id
        username = callback_query.from_user.username
        timestamp = datetime.datetime.now()
        file_name = 'Выходной за отработанный праздничный день.doc'
        perform_database_operations(user_id, username, timestamp, file_name)

        # Поиск и отправка файла
        file_path = "raports/sample_orders/Выходной за отработанный праздничный день.doc"
        if os.path.isfile(file_path):
            file = FSInputFile(file_path)
            keyboard_return = keyboard_go_back()
            await bot.send_document(callback_query.from_user.id, document=file,
                                    caption=f"Образец приказа: {file_name}", reply_markup=keyboard_return)
    except Exception as e:
        logger.error(f"An error occurred: {e}")

    await state.clear()


def register_sample_orders_handler():
    """Регистрируем handlers для работы в выходной день"""
    dp.register_message_handler(sample_orders)
    dp.register_message_handler(limit_form)
    dp.register_message_handler(contract_form)
