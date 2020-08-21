from aiogram import types
from loader import dp
from example_google_table import add_in_achive

from aiogram import types, filters
from loader import dp

@dp.message_handler(filters.RegexpCommandsFilter(regexp_commands=['studying_(\d\d_\d\d_\d\d\d\d)']))
async def send_welcome(message: types.Message, regexp_command):
    date_of_achive = regexp_command.group(1).replace("_", ".")
    await message.answer(f'Ачивка Studying за <code>{date_of_achive}</code> добавлена 🎓')
    await dp.bot.send_message(985485455,
                              f"Пользователь {message.from_user.full_name} добавил ачивку Studying за {date_of_achive}")
    await add_in_achive(date_of_achive, 'Studying', message.from_user.full_name, message.from_user.id)


# @dp.message_handler(text='/studying')
# async def work(message: types.Message):
#     await message.answer(text='Ачивка Studying добавлена 🎓')
#     await dp.bot.send_message(985485455, f"Пользователь {message.from_user.full_name} добавил ачивку Studying.")