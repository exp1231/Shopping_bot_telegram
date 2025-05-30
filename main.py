import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import settings
from handlers import dp
from utils.logger import setup_logger

# Настройка логгера
setup_logger()

# Инициализация бота
bot = Bot(token=settings.BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

async def on_startup(dp):
    from database.database import init_db
    await init_db()
    logging.info("Bot started")

async def on_shutdown(dp):
    logging.info("Bot stopped")
    await dp.storage.close()
    await dp.storage.wait_closed()

if __name__ == '__main__':
    executor.start_polling(
        dp,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True
    )