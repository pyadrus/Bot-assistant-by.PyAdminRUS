import json
import os

from aiogram import types
from aiogram.types import InputFile
from loguru import logger

from system.system import dp, bot


@dp.callback_query_handler(lambda c: c.data == 'checking_availability_of_reports')
async def checking_availability_of_reports(callback_query: types.CallbackQuery):
    """Проверка наличия рапортов"""
    # Путь к папке с файлами
    folder_path = "raports/rap_2024/02_feb_rap_2024"

    # Создаем список файлов в папке
    existing_files = os.listdir(folder_path)

    # Используем with open для открытия файла с использованием кодека utf-8
    with open('raports/rap_2024/02_feb_rap_2024/rap_2024.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        logger.info(data)

    # Создаем текстовый файл для записи отсутствующих файлов
    missing_files = []
    with open("отсутствующие_файлы.txt", "w", encoding='utf-8') as file:
        for code, description in data.items():
            filename = f"{code}.xls"
            if filename not in existing_files:
                missing_files.append(filename)
                file.write(f"Отсутствует файл {filename} - {description}\n")

    # Send the document using InputFile
    with open("отсутствующие_файлы.txt", "rb") as file:
        await bot.send_document(callback_query.from_user.id,
                                document=InputFile(file),
                                caption="Отсутствующие рапорта"
                                    )


def register_handlers_admin():
    dp.register_message_handler(checking_availability_of_reports, commands="checking_availability_of_reports")
