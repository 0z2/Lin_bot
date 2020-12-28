



async def get_results_for_period(user_name):
    amount_of_achievements_of_users_for_the_week_list = run_async(bot.loop, get_achievements_group_by_user_for_period())
    amount_of_achievements_of_user_for_the_week = amount_of_achievements_of_users_for_the_week_list[user_name]
    amount_of_achievements_of_user_for_the_week_count = Counter(amount_of_achievements_of_user_for_the_week)
    # print('Пользователь', user[1])
    message = 'Привет, вот твои результаты за неделю!\n\n'
    for name_of_achievement, amount_of_achievement in amount_of_achievements_of_user_for_the_week_count.items():
        message += (list_of_achievements[name_of_achievement] + ' - ' + str(amount_of_achievement) + '\n')
    return message
    # print(message)
