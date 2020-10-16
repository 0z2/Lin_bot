from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = [
        'Список команд: ',
        '/start - включить уведомления',
        '/pause - вылючить уведомления [скоро]\n',
        '/achievements_for_yesterday - ачивки за вчера',
        '/achievements_for_today - ачивки за сегодня\n',
        '/help - Получить справку\n',
        'Инструкция',
        'Ежедневно в 10:00',
        'будет приходить список из ачивок',
        'за предыдущий день.\n',
        'Бот в разработке. Если есть идеи фич, пиши прямо сюда, я увижу сообщение и постараюсь реализовать'
    ]
    await message.answer('\n'.join(text))
