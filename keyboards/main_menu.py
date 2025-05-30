from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("🛍️ Каталог товаров"))
    keyboard.add(KeyboardButton("🛒 Корзина"), KeyboardButton("📦 Мои заказы"))
    keyboard.add(KeyboardButton("ℹ️ Помощь"), KeyboardButton("⚙️ Настройки"))
    return keyboard