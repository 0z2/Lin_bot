import requests
from data.config import api_link
import schedule
import time
from datetime import datetime, date, timedelta

from data.config import users_id

def job():
    print("I'm working...")
    yesterday = date.today() - timedelta(days=1)
    yesterday_with_slash = yesterday.strftime("_%d_%m_%Y")
    yesterday_with_dots = yesterday.strftime("%d.%m.%Y")
    for user in users_id:
        try:
            notifying = requests.get(api_link + f'/sendMessage?chat_id={user[0]}&text=Привет, заполним ачивки за {yesterday_with_dots}?\n'
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
                                      )
        except Exception as err:
            pass

#schedule.every(1).minutes.do(job)
#schedule.every().hour.do(job)
schedule.every().day.at("10:00").do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)
#schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(50)