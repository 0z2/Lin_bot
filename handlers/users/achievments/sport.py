from aiogram import types, filters
from loader import dp
from example_google_table import add_in_achive

@dp.message_handler(filters.RegexpCommandsFilter(regexp_commands=['sport_(\d\d_\d\d_\d\d\d\d)']))
async def send_welcome(message: types.Message, regexp_command):
    date_of_achive = regexp_command.group(1)
    await message.answer(f'Ачивка Sport за <code>{date_of_achive}</code> добавлена ⛳')
    await dp.bot.send_message(985485455,
                              f"Пользователь {message.from_user.full_name} добавил ачивку Sport за {date_of_achive}")
    await add_in_achive(date_of_achive, 'Sport', message.from_user.full_name)

# @dp.message_handler(text='/sport')
# async def work(message: types.Message):
#     await message.answer(text='Ачивка Sport добавлена ⛳')
#     await dp.bot.send_message(985485455, f"Пользователь {message.from_user.full_name} добавил ачивку Sport.")