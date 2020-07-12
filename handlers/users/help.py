from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = [
        'Список команд: ',
        '/start - Начать диалог',
        '/help - Получить справку\n',
        'Список доступных ачивок:',
        '/work - за хорошую работу 🛠',
        '/sport - за занятия спортом ⛳',
        '/language - за изучение языков 🇺🇸',
        '/studying - за изучение прикладного, технического 🎓',
        '/health - за занятие здоровьем 💊'
    ]
    await message.answer('\n'.join(text))
