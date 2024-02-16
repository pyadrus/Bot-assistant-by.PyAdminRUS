import configparser

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils import executor

# from handlers.ai_handlers import register_send_gpt_handler
from handlers.days_off_handlers_2023 import register_days_off_callback_month_handler
from handlers.days_off_handlers_2022 import day_off_handler_22
from handlers.days_off_handlers_2024 import register_days_off_callback_month_handler_2024
from handlers.raport_handlers import register_raport_handler
from handlers.sample_orders_handlers import register_sample_orders_handler
from handlers.table_handlers import register_table_handler_handler
from keyboards.admin_keyboards.admin_keyboards import welcome_keyboard_admin
from keyboards.welcome_keyboard import welcome_keyboard
from messages.user_messages import welcome_text
from system.system import dp, bot
from loguru import logger

config = configparser.ConfigParser(empty_lines_in_values=False, allow_no_value=True)
# Считываем токен бота с файла config.ini
config.read("settings/config.ini")
bot_token = config.get('BOT_TOKEN', 'BOT_TOKEN')

logger.add('log/log.log')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message, state: FSMContext):
    """Обрабатываем команду /start"""
    await state.finish()  # Завершаем текущее состояние машины состояний
    await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
    main_keyboard = welcome_keyboard()  # Клавиатура приветствие
    await message.answer(welcome_text, reply_markup=main_keyboard)


@dp.message_handler(commands=['admin'])
async def admin_start_command(message: types.Message, state: FSMContext):
    """Админ панель"""
    await state.finish()
    await state.reset_state()
    main_keyboard = welcome_keyboard_admin()
    admin_welcome_text = ('Админ панель\n'
                          'Сделай свой выбор')
    await message.answer(admin_welcome_text, reply_markup=main_keyboard)


@dp.callback_query_handler(lambda c: c.data == "menu")
async def return_to_menu(callback_query: types.CallbackQuery, state: FSMContext):
    """Обрабатываем команду /menu или кнопку для возвращения в начальное меню"""
    await state.finish()  # Завершаем текущее состояние машины состояний
    await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
    main_keyboard = welcome_keyboard()  # Клавиатура приветствия
    await callback_query.message.answer(welcome_text, reply_markup=main_keyboard)


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


@dp.message_handler(state=FeedbackState.WAITING_FOR_FEEDBACK, content_types=types.ContentType.TEXT)
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
    await state.finish()


if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates=True)
        day_off_handler_22()
        register_table_handler_handler()
        return_to_menu()
        # register_send_gpt_handler() # GPT ответ
        register_raport_handler()  # Рапорт 2023
        register_days_off_callback_month_handler()  # Выходные дни в 2023 году
        register_days_off_callback_month_handler_2024()  # Выходные дни в 2024 году
        register_sample_orders_handler()  # Образцы приказов
    except Exception as e:
        logger.info(e)
