import os

from aiogram import F
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from aiogram.types import Message
from loguru import logger

from handlers.raport_handlers import perform_database_operations
from keyboards.welcome_keyboard import return_start_menu_keyboard, keyboard_for_report_2024, \
    create_feedback_and_return_to_menu_keyboard
from system.global_variables import Form_2024
from system.system import dp, bot, router


@router.callback_query(F.data == "rap_2024")
async def process_callback_month_2024(callback_query: types.CallbackQuery):
    """Кнопки с месяцами рапорта"""
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text="📅 Выберите месяц:",
        reply_markup=keyboard_for_report_2024()
    )

@router.callback_query(F.data == "01_jan_rap_2024")
async def process_callback_monthh_2024(callback_query: types.CallbackQuery, state: FSMContext):
    """Рапорта Март 2023"""
    month = callback_query.data
    logger.info(f'Запрос рапорта по месяцу {month}')
    await state.update_data(month=month)
    await bot.send_message(callback_query.from_user.id, "Введите код участка:")
    await state.set_state(Form_2024.district_2024)

@router.callback_query(F.data == "02_feb_rap_2024")
async def process_callback_monthh_2024(callback_query: types.CallbackQuery, state: FSMContext):
    """Рапорта Март 2023"""
    month = callback_query.data
    logger.info(f'Запрос рапорта по месяцу {month}')
    await state.update_data(month=month)
    await bot.send_message(callback_query.from_user.id, "Введите код участка:")
    await state.set_state(Form_2024.district_2024)

@router.callback_query(F.data == "03_mar_rap_2024")
async def process_callback_monthh_2024(callback_query: types.CallbackQuery, state: FSMContext):
    """Рапорта Март 2023"""
    month = callback_query.data
    logger.info(f'Запрос рапорта по месяцу {month}')
    await state.update_data(month=month)
    await bot.send_message(callback_query.from_user.id, "Введите код участка:")
    await state.set_state(Form_2024.district_2024)

@router.callback_query(F.data == "04_apr_rap_2024")
async def process_callback_monthh_2024(callback_query: types.CallbackQuery, state: FSMContext):
    """Рапорта Март 2023"""
    month = callback_query.data
    logger.info(f'Запрос рапорта по месяцу {month}')
    await state.update_data(month=month)
    await bot.send_message(callback_query.from_user.id, "Введите код участка:")
    await state.set_state(Form_2024.district_2024)

@router.callback_query(F.data == "05_may_rap_2024")
async def process_callback_monthh_2024(callback_query: types.CallbackQuery, state: FSMContext):
    """Рапорта Март 2023"""
    month = callback_query.data
    logger.info(f'Запрос рапорта по месяцу {month}')
    await state.update_data(month=month)
    await bot.send_message(callback_query.from_user.id, "Введите код участка:")
    await state.set_state(Form_2024.district_2024)

@router.callback_query(F.data == "06_jun_rap_2024")
async def process_callback_monthh_2024(callback_query: types.CallbackQuery, state: FSMContext):
    """Рапорта Март 2023"""
    month = callback_query.data
    logger.info(f'Запрос рапорта по месяцу {month}')
    await state.update_data(month=month)
    await bot.send_message(callback_query.from_user.id, "Введите код участка:")
    await state.set_state(Form_2024.district_2024)

@router.callback_query(F.data == "07_jul_rap_2024")
async def process_callback_monthh_2024(callback_query: types.CallbackQuery, state: FSMContext):
    """Рапорта Март 2023"""
    month = callback_query.data
    logger.info(f'Запрос рапорта по месяцу {month}')
    await state.update_data(month=month)
    await bot.send_message(callback_query.from_user.id, "Введите код участка:")
    await state.set_state(Form_2024.district_2024)

@router.callback_query(F.data == "08_aug_rap_2024")
async def process_callback_monthh_2024(callback_query: types.CallbackQuery, state: FSMContext):
    """Рапорта Март 2023"""
    month = callback_query.data
    logger.info(f'Запрос рапорта по месяцу {month}')
    await state.update_data(month=month)
    await bot.send_message(callback_query.from_user.id, "Введите код участка:")
    await state.set_state(Form_2024.district_2024)

@router.callback_query(F.data == "09_sep_rap_2024")
async def process_callback_monthh_2024(callback_query: types.CallbackQuery, state: FSMContext):
    """Рапорта Март 2023"""
    month = callback_query.data
    logger.info(f'Запрос рапорта по месяцу {month}')
    await state.update_data(month=month)
    await bot.send_message(callback_query.from_user.id, "Введите код участка:")
    await state.set_state(Form_2024.district_2024)

@router.callback_query(F.data == "10_oct_rap_2024")
async def process_callback_monthh_2024(callback_query: types.CallbackQuery, state: FSMContext):
    """Рапорта Март 2023"""
    month = callback_query.data
    logger.info(f'Запрос рапорта по месяцу {month}')
    await state.update_data(month=month)
    await bot.send_message(callback_query.from_user.id, "Введите код участка:")
    await state.set_state(Form_2024.district_2024)

@router.callback_query(F.data == "11_nov_rap_2024")
async def process_callback_monthh_2024(callback_query: types.CallbackQuery, state: FSMContext):
    """Рапорта Март 2023"""
    month = callback_query.data
    logger.info(f'Запрос рапорта по месяцу {month}')
    await state.update_data(month=month)
    await bot.send_message(callback_query.from_user.id, "Введите код участка:")
    await state.set_state(Form_2024.district_2024)

@router.callback_query(F.data == "12_dec_rap_2024")
async def process_callback_monthh_2024(callback_query: types.CallbackQuery, state: FSMContext):
    """Рапорта Март 2023"""
    month = callback_query.data
    logger.info(f'Запрос рапорта по месяцу {month}')
    await state.update_data(month=month)
    await bot.send_message(callback_query.from_user.id, "Введите код участка:")
    await state.set_state(Form_2024.district_2024)


list_of_plots_2024 = {110100: "Руководство",
                      110110: "Тех.служба",
                      110120: "Производ.служба",
                      110130: "Техн.служба",
                      110140: "СОТ и ТБ",
                      110150: "Маркшейдерская служба",
                      110160: "Геологическая служба",
                      110170: "ЭМС",
                      110191: "ПЭО",
                      110192: "ООТиЗП",
                      110194: "ООТ, ЗП и планирования",
                      110193: "Финансовый сектор",
                      110200: "Бухгалтерия",
                      110211: "Сектор договорной работы",
                      110220: "Сектор материально-технического снабжения",
                      110230: "Отдел кадров",
                      110240: "Сектор по социальным вопросам",
                      110250: "Юридический сектор",
                      120110: "Уч.№ 1",
                      120210: "УПР № 1",
                      120220: "УПР № 2",
                      120400: "Уч.ШТ",
                      120410: "УКТ № 1",
                      120420: "УКТ № 2",
                      120450: "УКТ",
                      120500: "Уч.РВР",
                      120520: "Уч.РВР №2",
                      120610: "Уч.МДГО № 1",
                      120700: "ВТБ",
                      120800: "Уч.ВР",
                      120900: "Участок профилактических работ по технике безопасности",
                      121000: "Водоотлив",
                      121010: "Участок стационарного оборудования №1",
                      121020: "Участок стационарного оборудования №2",
                      121030: "Электроцех",
                      121040: "Участок по ремонту забойного оборудования",
                      121050: "Участок по обслуживанию механизированной крепи",
                      121060: "Участок по ремонту вертикальных выработок",
                      121070: "Котельная",
                      121100: "Отдел технического контроля качества угля",
                      121110: "Участок автоматизированных систем управления и технологических процессов и связи",
                      121200: "Связь",
                      121400: "Административно-бытовой комбинат",
                      121500: "Здравпункт",
                      121600: "Участок 'Охрана'",
                      121710: "Автотранспортный участок",
                      121730: "Участок по формированию породного отвала",
                      121801: "Обогатительная фабрика",
                      100000: "Мобилизованные",
                    #   121810: "ИТР ОФ",
                    #   121820: "ОП ОФ",
                    #   121830: "Электроцех ОФ",
                    #   121840: "Монтажно-демонтажная группа ОФ",
                    #   121850: "Ремонтная группа ОФ",
                    #   121860: "Углехимическая лаборатория ОФ",
                    #   121870: "АБК ОФ",
                      121900: "Служба складского хозяйства",
                      121930: "Склад №1",
                      121940: "Склад №2",
                      121950: "Склад №3",
                      121960: "Склад строительных материалов",
                      121972: "Склад №4",
                      121970: "Угольный склад",
                      121971: "Лесной склад",
                      122100: "Участок 'Когенерационная электростанция'",
                      122200: "Участок по изготовлению и ремонту оборудования",
                      122400: "Участок строительно-монтажных работ",
                      130010: "Общежитие №1",
                      130020: "Гостиница 'Олимп'",
                      130030: "ПТК 'Донецкий'"}

report_no_text_found = ("🚫 <b>Файл не найден или рапорт не сформирован.</b>\n"
                        "Проверьте правильность введенного кода участка.\n\n"
                        "Нажмите <b>'↩️  Вернуться в начальное меню'</b>, чтобы повторить запрос.")

@router.message(Form_2024.district_2024)
async def process_district_2024(message: Message, state: FSMContext):
    data = await state.get_data()  # Получение данных из состояния
    month = data.get('month')  # Получаем месяц
    logger.info(f'Вопрос рапорта по месяцу {month}')
    district = message.text

    try:
        district_name = list_of_plots_2024[int(district)]
        # Запись в базу данных
        user_id = message.from_user.id
        username = message.from_user.username
        timestamp = str(message.date)
        file_name = district + '.xls'
        logger.info(f'Пользователь: username {username}, ID {user_id} в {timestamp} запросил рапорт участка {district_name}')
        perform_database_operations(user_id, username, timestamp, file_name)
        # Поиск и отправка файла
        file_path = f"raports/rap_2024/{month}/{district}.xls"
        if os.path.isfile(file_path):

            keyboard_return = return_start_menu_keyboard()
            if month == "01_jan_rap_2024":
                raport_month: str = "Январь 2024"
            if month == "02_feb_rap_2024":
                raport_month: str = "Февраль 2024"
            if month == "03_mar_rap_2024":
                raport_month: str = "Март 2024"
            if month == "04_apr_rap_2024":
                raport_month: str = "Апрель 2024"
            if month == "05_may_rap_2024":
                raport_month: str = "Май 2024"
            if month == "06_jun_rap_2024":
                raport_month: str = "Июнь 2024"
            if month == "07_jul_rap_2024":
                raport_month: str = "Июль 2024"
            if month == "08_aug_rap_2024":
                raport_month: str = "Август 2024"
            if month == "09_sep_rap_2024":
                raport_month: str = "Сентябрь 2024"
            if month == "10_oct_rap_2024":
                raport_month: str = "Октябрь 2024"
            if month == "11_nov_rap_2024":
                raport_month: str = "Ноябрь 2024"
            if month == "12_dec_rap_2024":
                raport_month: str = "Декабрь 2024"

            file = FSInputFile(file_path)

            await bot.send_document(message.from_user.id,
                                    document=file,
                                    caption=(f"<b>📅 {raport_month}\n\n"
                                                   f"Рапорт участка:</b> {district_name}"),
                                    parse_mode="HTML",
                                    reply_markup=keyboard_return)  # Отправка файла пользователю
        else:
            # Создаем клавиатуру с одной кнопкой "Отправить сообщение"
            keyboard = create_feedback_and_return_to_menu_keyboard()
            await message.answer(report_no_text_found, reply_markup=keyboard)
    except KeyError:
        # Создаем клавиатуру с одной кнопкой "Отправить сообщение"
        keyboard = create_feedback_and_return_to_menu_keyboard()
        await message.answer(report_no_text_found, reply_markup=keyboard)
    await state.clear()


def register_raport_handler_2024():
    """Регистрируем handlers для работы в выходной день"""
    dp.register_message_handler(process_callback_month_2024)
