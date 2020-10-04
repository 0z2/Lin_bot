import logging
from typing import Optional, Union

from aiogram import Bot, types

import schedule
import time
from datetime import datetime, date, timedelta

from work_with_gsheet import get_list_id_and_name_of_users

import asyncio


def run_async(loop: Optional[Union[asyncio.BaseEventLoop, asyncio.AbstractEventLoop]], coro):
    return loop.run_until_complete(coro)


def job(bot: Bot):
    print("I'm working...")
    yesterday = date.today() - timedelta(days=1)
    yesterday_with_slash = yesterday.strftime("_%d_%m_%Y")
    yesterday_with_dots = yesterday.strftime("%d.%m.%Y")
    users_id = run_async(bot.loop, get_list_id_and_name_of_users())
    for (user, *_) in users_id:
        try:
            run_async(bot.loop, bot.send_message(chat_id=user,
                                                 text=f'Привет, заполним ачивки за {yesterday_with_dots}?\n'
                                                      f'/work{yesterday_with_slash} - за хорошую работу 🛠\n'
                                                      f'/sport{yesterday_with_slash} - за занятия спортом 🏋🏻‍♀️🏋🏻\n'
                                                      f'/language{yesterday_with_slash} - за изучение языков 🇺🇸\n'
                                                      f'/studying{yesterday_with_slash} - за учёбу 🎓\n'
                                                      f'/health{yesterday_with_slash} - за занятие здоровьем 💊\n'
                                                      f'/proper_nutrition{yesterday_with_slash} - полезная еда 🥙\n'
                                                      f'/personal_care{yesterday_with_slash} - уход за собой 💆‍♀💇‍♂\n'
                                                      f'/music{yesterday_with_slash} - за занятие музыкой 🎸\n'
                                                      f'/delicious_house{yesterday_with_slash} - за вкусный дом 👩‍❤️‍👨🏡\n'
                                                      f'/yoga{yesterday_with_slash} - за занятия йогой 👩‍❤️‍👨🏡\n'))
            # notifying = requests.get(
            #     api_link + f'/sendMessage?chat_id={user}&text=
            # )
        except Exception as err:
            logging.exception(err)


bot = Bot(token="1267986653:AAEIxXafABfUFDDapLsEyjvNkeQ-6126q8Y", parse_mode=types.ParseMode.HTML)

#schedule.every(0.1).minutes.do(job, bot=bot)
# schedule.every().hour.do(job)
schedule.every().day.at("10:00").do(job, bot=bot)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(30)
