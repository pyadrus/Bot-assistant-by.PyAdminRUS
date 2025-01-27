import json
import os
from aiogram.types import FSInputFile
from aiogram import F
from aiogram import types

from loguru import logger

from system.system import dp, bot, router


@router.callback_query(F.data == "checking_availability_of_reports")
async def checking_availability_of_reports(callback_query: types.CallbackQuery):
    """Проверка наличия рапортов"""
    # Путь к папке с файлами
    folder_dic = ["01_jan_rap_2024", "02_feb_rap_2024", "03_mar_rap_2024", "04_apr_rap_2024", "05_may_rap_2024",
                  "06_jun_rap_2024", "07_jul_rap_2024", "08_aug_rap_2024", "09_sep_rap_2024", "10_oct_rap_2024",
                  "11_nov_rap_2024", "12_dec_rap_2024"]

    for dir in folder_dic:
        logger.info(dir)

        folder_path = f"raports/rap_2025/{dir}"

        if not os.path.exists(folder_path):
            logger.error(f"Directory {folder_path} does not exist")
            continue

        # Создаем список файлов в папке
        existing_files = os.listdir(folder_path)

        json_file_path = f'raports/rap_2025/{dir}/rap_2025.json'
        if not os.path.exists(json_file_path):
            logger.error(f"JSON file {json_file_path} does not exist")
            continue

        # Используем with open для открытия файла с использованием кодека utf-8
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            logger.info(data)

        # Создаем текстовый файл для записи отсутствующих файлов
        missing_files = []
        txt_file_path = f"отсутствующие_файлы_{dir}.txt"
        with open(txt_file_path, "w", encoding='utf-8') as file:
            for code, description in data.items():
                filename = f"{code}.xls"
                if filename not in existing_files:
                    missing_files.append(filename)
                    file.write(f"Отсутствует файл {filename} - {description}\n")

        if missing_files:
            # Send the document using InputFile
            file = FSInputFile(txt_file_path)

            # with open(txt_file_path, "rb") as file:
            await bot.send_document(callback_query.from_user.id,
                                    document=file,
                                    caption=f"Отсутствующие рапорта {dir}")
        else:
            await bot.send_message(callback_query.from_user.id, f"Все файлы на месте для {dir}.")


def register_handlers_admin():
    dp.register_message_handler(checking_availability_of_reports, commands="checking_availability_of_reports")
