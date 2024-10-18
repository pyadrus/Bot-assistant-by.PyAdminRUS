import asyncio
import configparser
import logging
import sys

from aiogram import types, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from loguru import logger
from aiogram.filters import Command
from handlers.admin_handlers.admin_handlers import register_handlers_admin
from handlers.days_off_handlers_2022 import day_off_handler_22
from handlers.days_off_handlers_2023 import register_days_off_callback_month_handler
from handlers.days_off_handlers_2024 import register_days_off_callback_month_handler_2024
from handlers.raport_handlers import register_raport_handler
from handlers.raport_handlers_2024 import register_raport_handler_2024
from handlers.sample_orders_handlers import register_sample_orders_handler
from handlers.table_handlers import register_table_handler_handler
from keyboards.admin_keyboards.admin_keyboards import welcome_keyboard_admin
from keyboards.welcome_keyboard import welcome_keyboard
from messages.user_messages import welcome_text
from system.system import dp, bot, router

config = configparser.ConfigParser(empty_lines_in_values=False, allow_no_value=True)

config.read("settings/config.ini")  # Считываем токен бота с файла config.ini
bot_token = config.get('BOT_TOKEN', 'BOT_TOKEN')

logger.add('log/log.log')


@dp.message(CommandStart())
async def start_command(message: types.Message, state: FSMContext):
    """Handle the /start command."""
    await state.clear()
    main_keyboard = welcome_keyboard()  # Welcome keyboard
    await bot.send_message(chat_id=message.chat.id, text=welcome_text, reply_markup=main_keyboard)

@router.message(Command("admin"))
async def admin_start_command(message: types.Message, state: FSMContext):
    """Админ панель"""
    await state.clear()
    main_keyboard = welcome_keyboard_admin()
    admin_welcome_text = ('Админ панель\n'
                          'Сделай свой выбор')
    await message.answer(admin_welcome_text, reply_markup=main_keyboard)

@router.callback_query(F.data == "menu")
async def return_to_menu(callback_query: types.CallbackQuery, state: FSMContext):
    """Обработайте команду /меню или кнопку, чтобы вернуться в главное меню."""
    try:

        await state.clear()
        main_keyboard = welcome_keyboard()  # Welcome keyboard
        await bot.send_message(callback_query.from_user.id, text=welcome_text, reply_markup=main_keyboard)

    except Exception as e:
        logger.exception(e)


class FeedbackState(StatesGroup):
    """Для обратной связи"""
    WAITING_FOR_FEEDBACK = State()

@router.callback_query(F.data == "feedback")
async def feedback_command_handler(callback_query: types.CallbackQuery, state: FSMContext):
    """Обратная связь с админом"""
    instructions = "Введите табельный номер и ваш вопрос ❓ Сообщения без табельного номера не будет обработано ❗️"
    await bot.send_message(chat_id=callback_query.from_user.id, text=instructions)
    await state.update_data(user_id=callback_query.from_user.id, username=callback_query.from_user.username)
    await state.set_state(FeedbackState.WAITING_FOR_FEEDBACK)

@router.message(FeedbackState.WAITING_FOR_FEEDBACK)
async def feedback_message_handler(message: types.Message, state: FSMContext):
    """Обработчик сообщений обратной связи"""
    user_feedback = message.text
    state_data = await state.get_data()  # получить данные пользователя из состояния
    user_id = state_data.get("user_id")
    username = state_data.get("username")
    # отправить сообщение в группу Telegram
    group_id = -1001768846220  # замените это значение на ID вашей группы
    feedback_message = f"Сообщение от пользователя {username} (ID: {user_id}):\n\n{user_feedback}"
    await bot.send_message(chat_id=group_id, text=feedback_message)
    confirmation_message = "Ваше сообщение отправлено!"  # отправить подтверждение пользователю
    await bot.send_message(chat_id=user_id, text=confirmation_message)
    # сбросить состояние обратно в None
    await state.clear()


async def main() -> None:
    try:
        await dp.start_polling(bot)
        day_off_handler_22()
        register_table_handler_handler()
        await return_to_menu()
        register_raport_handler()  # Рапорт 2023
        register_days_off_callback_month_handler()  # Выходные дни в 2023 году
        register_days_off_callback_month_handler_2024()  # Выходные дни в 2024 году
        register_sample_orders_handler()  # Образцы приказов
        register_raport_handler_2024()  # Рапорта 2024
        register_handlers_admin()  # Админ панель
    except Exception as e:
        logger.info(e)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
