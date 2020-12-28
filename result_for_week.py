import requests
from data.config import api_link
from typing import Optional, Union
from aiogram import Bot, types
import logging

import schedule
import time


import asyncio

from collections import Counter
from work_with_gsheet import get_achievements_group_by_user_for_period, get_list_id_and_name_of_users

def run_async(loop: Optional[Union[asyncio.BaseEventLoop, asyncio.AbstractEventLoop]], coro):
    return loop.run_until_complete(coro)

list_of_achievements = {'delicious_house': '👩‍❤️‍👨🏡 За вкусный дом',
                        'health': '💊 За занятие здоровьем',
                        'language': '🇺🇸 За изучение языков',
                        'music': '🎸 За занятие музыкой',
                        'personal_care': '💆‍♀💇‍♂ За уход за собой',
                        'proper_nutrition': '🥙 За правильное питание',
                        'sport': '🏋🏻‍♀️🏋🏻 За занятия спортом',
                        'studying': '🎓 За учёбу',
                        'work': '🛠 За хорошую работу',
                        'yoga': '🧘‍♂️За занятия йогой',
                        'voice': '🗣️ за работу над голосом',
                        'meditation': '🟣️ за медитацию',
                        'reading': '📖 за чтение',
                        }

# тут нужно добавить возможность перидать либо за неделю, либо за месяц и добавить два вызова, что бы одном случае
# писалось за неделю, а во втором за месяц
# либо просто передачу кол-ва дней, чтобы далее пользователь сам мог запрашивать. Хотя для пользователя лучше сделать
# возможность просмотра за этот месяц и предыдущий
def job(bot: Bot):
    try:
        list_of_users = run_async(bot.loop, get_list_id_and_name_of_users())
        for user in list_of_users:
            amount_of_achievements_of_users_for_the_week_list = run_async(bot.loop, get_achievements_group_by_user_for_period())
            amount_of_achievements_of_user_for_the_week = amount_of_achievements_of_users_for_the_week_list[user[1]]
            amount_of_achievements_of_user_for_the_week_count = Counter(amount_of_achievements_of_user_for_the_week)
            # print('Пользователь', user[1])
            message = 'Привет, вот твои результаты за неделю!\n\n'
            for name_of_achievement, amount_of_achievement in amount_of_achievements_of_user_for_the_week_count.items():
                message += (list_of_achievements[name_of_achievement] + ' - ' + str(amount_of_achievement) + '\n')
            # print(message)
            notifying = requests.get(api_link + f'/sendMessage?chat_id={user[0]}&text={message}')
            break  # для теста, чтобы отправилось только мне
    except Exception as err:
        logging.exception(err)

bot = Bot(token="1267986653:AAEIxXafABfUFDDapLsEyjvNkeQ-6126q8Y", parse_mode=types.ParseMode.HTML)

#schedule.every(0.1).minutes.do(job, bot=bot)
# schedule.every().hour.do(job)
schedule.every().day.at("23:37").do(job, bot=bot)
# schedule.every().monday.do(job)
#schedule.every().sunday.at("20:00").do(job)
# schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
