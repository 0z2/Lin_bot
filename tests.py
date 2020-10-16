# import requests
#
# from loader import db
#
# api_token = '1267986653:AAEIxXafABfUFDDapLsEyjvNkeQ-6126q8Y'
#
# params = requests.get('https://api.telegram.org/bot{}/sendMessage'.format(api_token), params=dict(
#    chat_id='214556467',
#    text='Бот в разработке. Если есть идеи фич, смело пиши на почту mozzgishere@gmail.com Постараюсь реализовать :) Первая рассылка с тегами придёт через пол часа.'
# ))
#
# print(params.content)
# 
# id = int(214556467)
# db.update_status('active', id)

yesterday_with_dots = 123
yesterday_with_slash = 456
text = (f'Привет, заполним ачивки за {yesterday_with_dots}?\n'
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

print(text)