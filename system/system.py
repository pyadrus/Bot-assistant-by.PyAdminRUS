from aiogram import Bot, Dispatcher, Router
import configparser

from aiogram.fsm.storage.memory import MemoryStorage

config = configparser.ConfigParser(empty_lines_in_values=False, allow_no_value=True)
# Считываем токен бота с файла config.ini
config.read("settings/config.ini")
bot_token = config.get('BOT_TOKEN', 'BOT_TOKEN')


# Инициализация бота и диспетчера
bot = Bot(token=bot_token)

# parse_mode="HTML" - разметка сообщения HTML
storage = MemoryStorage()  # Хранилище
dp = Dispatcher(storage=storage)

router = Router()
dp.include_router(router)
