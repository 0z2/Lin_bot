from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db
import sqlite3


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    #await message.answer(f'Привет, {message.from_user.full_name}! Чтобы узнать список доступных комманд напиши /help')
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id, name=name)
    except sqlite3.IntegrityError as err:
        print(err)

    count_users = db.count_users()[0]
    await message.answer(
        "\n".join([
            f'Привет, {message.from_user.full_name}!',
            'Ты был занесен в базу',
            f'В базе <b>{count_users}</b> пользователей',
        ])
    )


