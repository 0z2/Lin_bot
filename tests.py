import requests

from loader import db

api_token = '1267986653:AAEIxXafABfUFDDapLsEyjvNkeQ-6126q8Y'

params = requests.get('https://api.telegram.org/bot{}/sendMessage'.format(api_token), params=dict(
   chat_id='214556467',
   text='Бот в разработке. Если есть идеи фич, смело пиши на почту mozzgishere@gmail.com Постараюсь реализовать :) Первая рассылка с тегами придёт через пол часа.'
))

print(params.content)

id = int(214556467)
db.update_status('active', id)