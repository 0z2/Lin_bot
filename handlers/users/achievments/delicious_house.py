from aiogram import types, filters
from loader import dp
from example_google_table import add_in_achive

@dp.message_handler(filters.RegexpCommandsFilter(regexp_commands=['delicious_house_(\d\d_\d\d_\d\d\d\d)']))
async def send_welcome(message: types.Message, regexp_command):
    date_of_achive = regexp_command.group(1).replace("_", ".")
    await message.answer(f'Ачивка <b>Delicious_house</b> за <b>{date_of_achive}</b> добавлена 👩‍❤️‍👨🏡')
    await dp.bot.send_message(985485455,
                              f"Пользователь {message.from_user.full_name} добавил ачивку Delicious_house за {date_of_achive}")
    await add_in_achive(date_of_achive, 'Delicios house', message.from_user.full_name)

#async def work(message: types.Message, regexp):
    #regexp_args = regexp
    #await message.answer(text='Ачивка Work добавлена 🛠')
    #await dp.bot.send_message(985485455, f"Пользователь {message.from_user.full_name} добавил ачивку Work {regexp_args}.")