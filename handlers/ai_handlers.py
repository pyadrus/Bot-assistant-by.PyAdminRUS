# from aiogram import types
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import StatesGroup, State

# import g4f
# from keyboards.welcome_keyboard import keyboard_go_back
# from system.system import dp
# from loguru import logger

# class FormGPT(StatesGroup):
    # district_gpt = State()


# @dp.callback_query_handler(lambda c: c.data in ['feedback_ai'])
# async def send_gpt(callback_query: types.CallbackQuery, state: FSMContext):
    # await state.finish()  # Finish the current state
    # await FormGPT.district_gpt.set()
    # markup = keyboard_go_back()  # Keyboard to go back to the initial menu
    # await callback_query.message.answer("Задайте свой вопрос ИИ", reply_markup=markup)


# @dp.message_handler(state=FormGPT.district_gpt)
# async def process_district_gpt(message: types.Message, state: FSMContext):
    # try:
        # logger.info("Before processing: State = {}", await state.get_state())
        # user_question = message.text
        # response = g4f.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user",
                                                # "content": f"{user_question}"}],
                                    #  stream=True)
        # response_text = []
        # for message_grt in response:
            # response_text.append(message_grt)
        # print(response_text)
        # await message.answer(response_text[-1], reply_markup=keyboard_go_back())
        # await state.finish()  # Finish the current state
        # logger.info("After processing: State = {}", await state.get_state())
    # except Exception as e:
        # logger.info(e)

# def register_send_gpt_handler():
    # """Register handlers for the bot"""
    # dp.register_message_handler(process_district_gpt)
    # dp.register_message_handler(send_gpt)
