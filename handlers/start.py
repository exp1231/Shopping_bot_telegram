from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from database.crud import get_or_create_user
from keyboards.main_menu import main_menu_keyboard
from loader import dp


@dp.message_handler(Command("start"), state="*")
async def cmd_start(message: types.Message, state: FSMContext):
    await state.finish()

    user = await get_or_create_user(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )

    await message.answer(
        f"👋 Привет, {message.from_user.first_name}!\n"
        "Я - ваш умный помощник для покупок. Что вы хотите сделать?",
        reply_markup=main_menu_keyboard()
    )