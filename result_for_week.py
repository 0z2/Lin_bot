import requests
from data.config import api_link

from collections import Counter
from work_with_gsheet import get_list_id_and_name_of_users
from work_with_gsheet import get_achievements_group_by_user_for_period

list_of_achievements = {'delicious_house': 'За вкусный дом 👩‍❤️‍👨🏡',
                        'health': 'За занятие здоровьем 💊',
                        'language': 'За изучение языков 🇺🇸',
                        'music': 'За занятие музыкой 🎸',
                        'personal_care': 'За уход за собой 💆‍♀💇‍♂',
                        'proper_nutrition': 'За правильное питание 🥙',
                        'sport': 'За занятия спортом 🏋🏻‍♀️🏋🏻',
                        'studying': 'За учёбу 🎓',
                        'work': 'За хорошую работу 🛠',
                        'yoga': 'За занятия йогой 🧘‍♂️',

                        }

# тут нужно добавить возможность перидать либо за неделю, либо за месяц и добавить два вызова, что бы одном случае
# писалось за неделю, а во втором за месяц
# либо просто передачу кол-ва дней, чтобы далее пользователь сам мог запрашивать. Хотя для пользователя лучше сделать
# возможность просмотра за этот месяц и предыдущий
def send_achievements_of_users():
    list_of_users = get_list_id_and_name_of_users()
    for user in list_of_users:
        amount_of_achievements_of_user_for_the_week = Counter(get_achievements_group_by_user_for_period()[user[1]])
        # print('Пользователь', user[1])
        message = 'Привет, вот твои результаты за неделю!\n\n'
        for name_of_achievement, amount_of_achievement in amount_of_achievements_of_user_for_the_week.items():
            message += (list_of_achievements[name_of_achievement] + ' - ' + str(amount_of_achievement) + '\n')
        # print(message)
        notifying = requests.get(api_link + f'/sendMessage?chat_id={user[0]}&text={message}')
        break  # для теста, чтобы отправилось только мне

send_achievements_of_users()