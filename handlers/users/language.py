from aiogram import types
from loader import dp

from aiogram import types, filters
from loader import dp

@dp.message_handler(filters.RegexpCommandsFilter(regexp_commands=['language_(\d\d_\d\d_\d\d\d\d)']))
async def send_welcome(message: types.Message, regexp_command):
    date_of_achive = regexp_command.group(1)
    await message.reply(f'Ачивка Language за <code>{date_of_achive}</code> добавлена 🇺🇸')
    await dp.bot.send_message(985485455,
                              f"Пользователь {message.from_user.full_name} добавил ачивку Language за {date_of_achive}")


# @dp.message_handler(text='/language')
# async def work(message: types.Message):
#     await message.answer(text='Ачивка Language добавлена 🇺🇸')
#     await dp.bot.send_message(985485455, f"Пользователь {message.from_user.full_name} добавил ачивку Language.")