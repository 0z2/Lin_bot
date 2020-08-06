from aiogram import types, filters
from loader import dp

@dp.message_handler(filters.RegexpCommandsFilter(regexp_commands=['delicious_house_(\d\d_\d\d_\d\d\d\d)']))
async def send_welcome(message: types.Message, regexp_command):
    date_of_achive = regexp_command.group(1)
    await message.answer(f'Ачивка Delicious_house за <code>{date_of_achive}</code> добавлена 👩‍❤️‍👨🏡')
    await dp.bot.send_message(985485455,
                              f"Пользователь {message.from_user.full_name} добавил ачивку Delicious_house за {date_of_achive}")

#async def work(message: types.Message, regexp):
    #regexp_args = regexp
    #await message.answer(text='Ачивка Work добавлена 🛠')
    #await dp.bot.send_message(985485455, f"Пользователь {message.from_user.full_name} добавил ачивку Work {regexp_args}.")