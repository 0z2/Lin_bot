from aiogram import types, filters
from loader import dp

@dp.message_handler(filters.RegexpCommandsFilter(regexp_commands=['sport_(\d\d_\d\d_\d\d\d\d)']))
async def send_welcome(message: types.Message, regexp_command):
    date_of_achive = regexp_command.group(1).replace("_", ".")
    await message.answer(f'Ачивка S<b>port</b> за <b>{date_of_achive}</b> добавлена ⛳')
    await dp.bot.send_message(985485455,
                              f"Пользователь {message.from_user.full_name} добавил ачивку Sport за {date_of_achive}")

# @dp.message_handler(text='/sport')
# async def work(message: types.Message):
#     await message.answer(text='Ачивка Sport добавлена ⛳')
#     await dp.bot.send_message(985485455, f"Пользователь {message.from_user.full_name} добавил ачивку Sport.")