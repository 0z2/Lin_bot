import requests
from config import api_link
import schedule
import time
from datetime import datetime, date, timedelta

from config import users_id

def job():
    print("I'm working...")
    yesterday = date.today() - timedelta(days=1)
    yesterday_with_slash = yesterday.strftime("_%d_%m_%Y")
    yerstaday_with_dots = yesterday.strftime("%d.%m.%Y")
    for user in users_id:
        try:
            notifiying = requests.get(api_link + f'/sendMessage?chat_id={user}&text=Привет, заполним ачивки за {yerstaday_with_dots}?\n'
                                                 f'/work{yesterday_with_slash} - за хорошую работу 🛠\n'
                                                 f'/sport{yesterday_with_slash} - за занятия спортом ⛳\n'
                                                 f'/language{yesterday_with_slash} - за изучение языков 🇺🇸\n'
                                                 f'/studying{yesterday_with_slash} - за изучение прикладного, технического 🎓\n'
                                                 f'/health{yesterday_with_slash} - за занятие здоровьем 💊\n'
                                      )
        except Exception as err:
            pass

schedule.every(0.2).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:00").do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)
#schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)