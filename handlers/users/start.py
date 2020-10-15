from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db
import sqlite3


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}! Чтобы узнать список доступных комманд напиши /help')
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id, name=name)
    except sqlite3.IntegrityError as err:
        print(err)



    count_users = db.count_users()
    await message.answer(
        "\n".join([
            f'О том как вести ачивки читай тут https://vc.ru/services/126297-kak-s-pomoshchyu-miro-i-emodzi-stat-v-100500-raz-produktivnee \n',
            f'Я тоже начинал вести ачивки в miro, как предлагается в статье, но потом стало лень туда заходить и '
            f'поэтому сделал бота. Может и тебе зайдёт 😉\n \n'
            f'Если есть идеи фич, пиши прямо сюда, я увижу сообщение и постараюсь реализовать 😊'
        ])
    )
    await dp.bot.send_message(985485455,
                              f"Пользователь {message.from_user.full_name} был добавлен в базу")


