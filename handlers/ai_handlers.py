from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from gigachat import GigaChat
from langchain.chat_models.gigachat import GigaChat
from langchain.schema import HumanMessage, SystemMessage

from keyboards.welcome_keyboard import keyboard_go_back
from system.system import dp


class FormGPT(StatesGroup):
    district_gpt = State()


@dp.callback_query_handler(lambda c: c.data in ['feedback_ai'])
async def send_gpt(callback_query: types.CallbackQuery, state: FSMContext):
    await state.finish()  # Завершаем текущее состояние машины состояний
    await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
    await FormGPT.district_gpt.set()
    markup = keyboard_go_back()  # Клавиатура возврата в начальное меню
    await callback_query.message.answer("Задайте свой вопрос ИИ", reply_markup=markup)


@dp.message_handler(state=FormGPT.district_gpt)
async def process_district_gpt(message: types.Message, state: FSMContext):
    user_question = message.text
    chat = GigaChat(credentials='ZGNjMGU3YzYtNjZhOC00MjYwLWI1ODctYTUxYzNjZWNmYmZkOjJkNGIxMWRhLTY5ZjUtNDE5YS1hMmExLWNkNjMzODJkNTRhMw==', verify_ssl_certs=False)
    messages = [SystemMessage(content="Ты эмпатичный бот-психолог мужского пола, который помогает пользователю решить его проблемы.")]
    messages.append(HumanMessage(content=user_question))
    res = chat(messages)
    markup = keyboard_go_back()  # Клавиатура возврата в начальное меню
    await message.answer(res.content, reply_markup=markup)
    await state.finish()


def register_send_gpt_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(process_district_gpt)
    dp.register_message_handler(send_gpt)