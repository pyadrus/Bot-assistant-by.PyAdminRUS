import configparser
# import math

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor

from handlers.days_off_handlers_2022 import day_off_handler_22
from keyboards.welcome_keyboard import welcome_keyboard
from system.system import dp, bot
from handlers import raport_handlers  # Рапорта (не удалять)
from handlers import days_off_handlers  # Рапорта (не удалять)

config = configparser.ConfigParser(empty_lines_in_values=False, allow_no_value=True)
# Считываем токен бота с файла config.ini
config.read("settings/config.ini")
bot_token = config.get('BOT_TOKEN', 'BOT_TOKEN')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    """Обрабатываем команду /start"""
    main_keyboard = welcome_keyboard()  # Клавиатура приветствие
    await message.reply("Выберите пункт:", reply_markup=main_keyboard)


class FeedbackState(StatesGroup):
    """Для обратной связи"""
    WAITING_FOR_FEEDBACK = State()


@dp.callback_query_handler(lambda c: c.data in ['feedback'])
async def feedback_command_handler(callback_query: types.CallbackQuery, state: FSMContext):
    """Обратная связь с админом"""
    instructions = "Введите табельный номер и ваш вопрос ❓ Сообщения без табельного номера не будет обработано ❗️"
    await bot.send_message(chat_id=callback_query.from_user.id, text=instructions)
    await FeedbackState.WAITING_FOR_FEEDBACK.set()
    await state.update_data(user_id=callback_query.from_user.id, username=callback_query.from_user.username)


# обработчик сообщений обратной связи
@dp.message_handler(state=FeedbackState.WAITING_FOR_FEEDBACK, content_types=types.ContentType.TEXT)
async def feedback_message_handler(message: types.Message, state: FSMContext):
    user_feedback = message.text

    # получить данные пользователя из состояния
    state_data = await state.get_data()
    user_id = state_data.get("user_id")
    username = state_data.get("username")

    # отправить сообщение в группу Telegram
    group_id = -1001768846220  # замените это значение на ID вашей группы
    feedback_message = f"Сообщение от пользователя {username} (ID: {user_id}):\n\n{user_feedback}"
    await bot.send_message(chat_id=group_id, text=feedback_message)

    # отправить подтверждение пользователю
    confirmation_message = "Ваше сообщение отправлено!"
    await bot.send_message(chat_id=user_id, text=confirmation_message)

    # сбросить состояние обратно в None
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    day_off_handler_22()
