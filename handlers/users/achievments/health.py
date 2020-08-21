from aiogram import types, filters
from loader import dp
from example_google_table import add_in_achive

@dp.message_handler(filters.RegexpCommandsFilter(regexp_commands=['health_(\d\d_\d\d_\d\d\d\d)']))
async def add_achive(message: types.Message, regexp_command):
    date_of_achive = regexp_command.group(1).replace("_", ".")
    await message.answer(f'Ачивка Health за <code>{date_of_achive}</code> добавлена 💊')
    await dp.bot.send_message(985485455,
                              f"Пользователь {message.from_user.full_name} добавил ачивку Health за {date_of_achive}")
    await add_in_achive(date_of_achive, 'Health', message.from_user.full_name, message.from_user.id)

# @dp.message_handler(text='/health')
# async def work(message: types.Message):
#     await message.answer(text='Ачивка Health добавлена 💊')
#     await dp.bot.send_message(985485455, f"Пользователь {message.from_user.full_name} добавил ачивку Health.")