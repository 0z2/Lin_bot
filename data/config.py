import os

from dotenv import load_dotenv
from example_google_table import users

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
admins = [
    985485455
]

# for working notifications
api_link = 'https://api.telegram.org/bot1267986653:AAEIxXafABfUFDDapLsEyjvNkeQ-6126q8Y'
users_id = users.id_and_name_of_users()




ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
