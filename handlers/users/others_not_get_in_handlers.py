from aiogram import types
from loader import dp


@dp.message_handler()
async def bot_echo(message: types.Message):
    #await message.answer(message.text)
    await dp.bot.send_message(985485455,
                              f"Пользователь {message.from_user.full_name} написал: {message.text}")
