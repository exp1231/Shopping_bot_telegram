import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "").split(',')))
    DATABASE_URL = os.getenv("DATABASE_URL")
    PAYMENT_TOKEN = os.getenv("PAYMENT_TOKEN")

    class Redis:
        HOST = os.getenv("REDIS_HOST", "localhost")
        PORT = int(os.getenv("REDIS_PORT", 6379))
        DB = int(os.getenv("REDIS_DB", 0))


settings = Settings()