import logging
from typing import Optional, Union

from aiogram import Bot, types

import schedule
import time

# from work_with_gsheet import get_list_id_and_name_of_users
from loader import db
import sqlite3

import asyncio

from handlers.users.get_list_achievements import message_with_achievements


def run_async(loop: Optional[Union[asyncio.BaseEventLoop, asyncio.AbstractEventLoop]], coro):
    return loop.run_until_complete(coro)

def job(bot: Bot):
    print("I'm working...")
    try:
        users_id = db.select_all_users()
    except sqlite3.IntegrityError as err:
        print(err)
    for user_id, user_name, status in users_id:
        if status == 'active':
            try:
                print(user_name)
                run_async(bot.loop, bot.send_message(chat_id=user_id,
                                                     text=message_with_achievements()
                                                     ))
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
    time.sleep(1)
