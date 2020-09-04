from utils.set_bot_commands import set_default_commands
from result_for_week import send_achievements_of_users

async def on_startup(dp):
    import filters
    import middlewares

    filters.setup(dp)
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    #from result_for_week import test123
    await on_startup_notify(dp)
    await set_default_commands(dp)
    #await test123(dp)



if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
