import requests
from data.config import api_link
from collections import Counter
from example_google_table import users # это экземпляр класса, а не список юзеров
from example_google_table import achievements_group_by_user_for_week


list_of_achievements = {'delicious_house': 'За вкусный дом 👩‍❤️‍👨🏡',
                       'health': 'За занятие здоровьем 💊',
                       'language': 'За изучение языков 🇺🇸',
                       'music': 'За занятие музыкой 🎸',
                       'personal_care': 'Уход за собой 💆‍♀💇‍♂',
                       'proper_nutrition': 'За правильное питание 🥙',
                       'sport': 'За занятия спортом 🏋🏻‍♀️🏋🏻',
                       'studying': 'За учёбу 🎓',
                       'work': 'За хорошую работу 🛠'
                       }

def print_achievements_of_users():
    list_of_users = users.id_and_name_of_users()
    for user in list_of_users:
        achievements_for_the_week_of_user = Counter(achievements_group_by_user_for_week[user[1]])
        #print('Пользователь', user[1])
        message = 'Привет, вот твои результаты за неделю!\n\n'
        for letter, count in achievements_for_the_week_of_user.items():
            message += (list_of_achievements[letter] + ' - ' + str(count) + '\n')
        #print(message)
        notifying = requests.get(api_link + f'/sendMessage?chat_id={user[0]}&text={message}')

