from aiogram import types, filters
from loader import dp
from work_with_gsheet import add_new_achievement

@dp.message_handler(filters.RegexpCommandsFilter(regexp_commands=['reading_(\d\d_\d\d_\d\d\d\d)']))
async def send_welcome(message: types.Message, regexp_command):
    date_of_achive = regexp_command.group(1).replace("_", ".")
    await message.answer(f'Ачивка Reading за <code>{date_of_achive}</code> добавлена 📖')
    await dp.bot.send_message(985485455,
                              f"Пользователь {message.from_user.full_name} добавил ачивку Reading за {date_of_achive}")
    await add_new_achievement(date_of_achive, 'reading', message.from_user.full_name, message.from_user.id)
