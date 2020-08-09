import requests
from data.config import api_link
import schedule
import time
from datetime import datetime, date, timedelta

from data.config import users_id

# def job():
#     print("I'm working...")
#     yesterday = date.today() - timedelta(days=1)
#     yesterday_with_slash = yesterday.strftime("_%d_%m_%Y")
#     yesterday_with_dots = yesterday.strftime("%d.%m.%Y")
#     for user in users_id:
#         try:
notifying = requests.get(api_link + f'/sendPhoto?chat_id=722292238&photo=https://ibb.co/vDqf1c0&caption=Привет, вот твои результаты за неделю!\n\n'
                                     f'За хорошую работу 🛠 - 5\n'
                                     #f'За занятия спортом 🏋🏻‍♀️🏋🏻\n'
                                     #f'За изучение языков 🇺🇸\n'
                                     f'За учёбу 🎓 - 3\n'
                                     #f'За занятие здоровьем 💊\n'
                                     #f'Полезная еда 🥙\n'
                                     #f'Уход за собой 💆‍♀💇‍♂\n'
                                     #f'За занятие музыкой 🎸\n'
                                     f'За вкусный дом 👩‍❤️‍👨🏡 - 5\n\n'
                                     f'Так держать! ❤'
                                      )
print(notifying)
#         except Exception as err:
#             pass
#
# #schedule.every(0.2).minutes.do(job)
# #schedule.every().hour.do(job)
# schedule.every().day.at("10:00").do(job)
# #schedule.every().monday.do(job)
# #schedule.every().wednesday.at("13:15").do(job)
# #schedule.every().minute.at(":17").do(job)
#
# while True:
#     schedule.run_pending()
#     time.sleep(50)
