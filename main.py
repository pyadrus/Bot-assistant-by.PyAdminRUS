import configparser
import math

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from handlers import raport_handlers  # Рапорта (не удалять)
from system import dp, bot

config = configparser.ConfigParser(empty_lines_in_values=False, allow_no_value=True)
# Считываем токен бота с файла config.ini
config.read("settings/config.ini")
bot_token = config.get('BOT_TOKEN', 'BOT_TOKEN')


class Form(StatesGroup):
    month = State()
    district = State()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    """Обрабатываем команду /start"""
    main_keyboard = InlineKeyboardMarkup()
    raport_button = InlineKeyboardButton(text='🔨Рапорта 2023', callback_data='rap')
    days_off_button = InlineKeyboardButton(text='📅 Выходные дни 2023', callback_data='days_off')
    feedback_button = InlineKeyboardButton(text='⁉️ Задать вопрос, напомнить, замечание', callback_data='feedback')
    main_keyboard.row(raport_button, days_off_button)
    main_keyboard.row(feedback_button)
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


@dp.callback_query_handler(lambda c: c.data in ['days_off'])
async def days_off_callback_month(callback_query: types.CallbackQuery):
    """Плановые и выходные дни в Мае 2023"""
    keyboard = InlineKeyboardMarkup()
    may_button = InlineKeyboardButton(text='📅 Май 2023', callback_data='may_days_off')
    june_button = InlineKeyboardButton(text='📅 Июнь 2023', callback_data='june_days_off')
    keyboard.row(may_button, june_button)

    await bot.send_message(callback_query.from_user.id, "📅 Выберите месяц:", reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data in ['may_days_off'])
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    selected_month = callback_query.data
    await state.update_data(month=selected_month)
    await Form.district.set()

    norm_working_days = 19
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)

    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в Мае 2023:</code><b> {norm_working_days}</b>\n"
                                  f"\n<code>📅 Выходные:</code><b> 6, 7, 8, 13, 14, 20, 21, 27, 28</b>\n"
                                  f"<code>📅 Праздничные:</code><b> 1, 9, 11</b>\n"
                                  f"\n<code>📅 Выходные поверхность:</code><b> 1, 6, 7, 8, 9, 10, 13, 14, 20, 21, 27, 28</b>\n"
                                  f"<code>📅 Выходные подземные:</code><b>1, 3, 7, 8, 9, 11, 14, 17, 21, 24, 28</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML")

    await state.finish()


@dp.callback_query_handler(lambda c: c.data in ['june_days_off'])
async def days_off_process_callback_monthh(callback_query: types.CallbackQuery, state: FSMContext):
    selected_month = callback_query.data
    await state.update_data(month=selected_month)
    await Form.district.set()

    norm_working_days = 20
    norm_working_hours = norm_working_days * 8
    norm_hours_12h_shift = math.ceil(norm_working_hours / 12)
    norm_hours_24h_shift = math.ceil(norm_working_hours / 24)

    response_message = callback_query.message
    await response_message.answer(f"<code>✅ Норма выходов в Июне 2023:</code><b> {norm_working_days}</b>\n"
                                  f"\n<code>📅 Выходные:</code><b> 3, 5, 10, 11, 17, 18, 24, 25</b>\n"
                                  f"<code>📅 Праздничные:</code><b> 4, 12</b>\n"
                                  f"\n<code>📅 Выходные поверхность:</code><b> 3, 4, 5, 10, 11, 12, 17, 18, 24, 25</b>\n"
                                  f"<code>📅 Выходные подземные:</code><b>4, 5, 7, 11, 12, 14, 18, 21, 25, 28</b>\n"
                                  f"\n<code>🔨 Выходов для 6 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 8 часовых:</code><b> {norm_working_days}</b>\n"
                                  f"<code>🔨 Выходов для 12 часовых:</code><b> {norm_hours_12h_shift}</b>\n"
                                  f"<code>🔨 Выходов для 24 часовых:</code><b> {norm_hours_24h_shift}</b>\n"
                                  f"\nНажмите /start, чтобы вернуться в начало", parse_mode="HTML")

    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
