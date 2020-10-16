from aiogram import types, filters
from loader import dp

from datetime import date, timedelta


def message_with_achievements(day=1):
    yesterday = date.today() - timedelta(days=day)
    yesterday_with_slash = yesterday.strftime("_%d_%m_%Y")
    yesterday_with_dots = yesterday.strftime("%d.%m.%Y")
    return (f'Привет, заполним ачивки за {yesterday_with_dots}?\n'
            f'/work{yesterday_with_slash} - за хорошую работу 🛠\n'
            f'/sport{yesterday_with_slash} - за занятия спортом 🏋🏻‍♀️🏋🏻\n'
            f'/language{yesterday_with_slash} - за изучение языков 🇺🇸\n'
            f'/studying{yesterday_with_slash} - за учёбу 🎓\n'
            f'/health{yesterday_with_slash} - за занятие здоровьем 💊\n'
            f'/proper_nutrition{yesterday_with_slash} - полезная еда 🥙\n'
            f'/personal_care{yesterday_with_slash} - уход за собой 💆‍♀💇‍♂\n'
            f'/music{yesterday_with_slash} - за занятие музыкой 🎸\n'
            f'/delicious_house{yesterday_with_slash} - за вкусный дом 👩‍❤️‍👨🏡\n'
            f'/yoga{yesterday_with_slash} - за занятия йогой 👩‍❤️‍👨🏡\n'
            f'/voice{yesterday_with_slash} - за работу над голосом 🗣️\n'
            f'/meditation{yesterday_with_slash} - за медитацию 💫️\n')

days = {'/achievements_for_yesterday': 1, '/achievements_for_today': 0}
@dp.message_handler(commands=['achievements_for_yesterday', 'achievements_for_today'])
async def cmd_handler(message: types.Message):
    command = message.get_command()
    # в зависимости от команды передаю дальше из словаря либо 1 либо 0, в зависимости за какой день список ачивок нужно дать
    await message.answer(message_with_achievements(days[command]))
    await dp.bot.send_message(985485455,
                              f"Пользователь {message.from_user.full_name} запросил список ачивок")


