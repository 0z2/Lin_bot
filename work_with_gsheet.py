# статья с описанием работы - https://habr.com/ru/post/483302/
# Подключаем библиотеки
import asyncio

# для работы с гугл таблицами
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

from datetime import datetime, timedelta

CREDENTIALS_FILE = 'data/google_sheet_auth.json'  # Имя файла с закрытым ключом
# Читаем ключи из файла
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                               ['https://www.googleapis.com/auth/spreadsheets',
                                                                'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())  # Авторизуемся в системе
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)  # Выбираем работу с таблицами и 4 версию API
spreadsheetId = '1pxrkIrlNgUnhTK1jj00iYxu5jlpl79nEy77yvntckvo'  # spreadsheet['spreadsheetId'] # сохраняем идентификатор файла
print('https://docs.google.com/spreadsheets/d/' + spreadsheetId)
driveService = apiclient.discovery.build('drive', 'v3', http=httpAuth)  # Выбираем работу с Google Drive и 3 версию API


async def get_results_from_gsheet(ranges):
    await asyncio.sleep(1)
    # возвращает значения из переданного диапазона
    result = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheetId,
                                                      ranges=ranges,
                                                      valueRenderOption='FORMATTED_VALUE',
                                                      dateTimeRenderOption='FORMATTED_STRING').execute()
    return result


async def get_amount_of_users():
    await asyncio.sleep(1)
    ranges = ["Пользователи!I1:I1"]
    results = await get_results_from_gsheet(ranges)
    sheet_values = results['valueRanges'][0]['values']
    return sheet_values[0][0]


async def get_list_id_and_name_of_users():
    await asyncio.sleep(1)
    ranges = ["Пользователи!B2:C100"]  # тут нужно увеличить кол-во получаемых id
    results = await get_results_from_gsheet(ranges)
    sheet_values = results['valueRanges'][0]['values']
    return sheet_values


async def get_amount_of_achievements():
    await asyncio.sleep(1)
    # эту функция нужная для того чтобы узнать в какую строку записывать следующую ачивку
    # возвращает номер последней строки с записью
    ranges = ["Ачивки!I1:I1"]
    results = await get_results_from_gsheet(ranges)
    sheet_values = results['valueRanges'][0]['values']
    return sheet_values[0][0]


async def get_list_of_achievements():
    await asyncio.sleep(1)
    # Получение списка ачивок, даты и пользователя
    last_line_with_achievement = await get_amount_of_achievements()
    ranges = [f"Ачивки!B2:D{last_line_with_achievement}"]  # тут нужно увеличить кол-во получаемых id
    results = await get_results_from_gsheet(ranges)
    sheet_values = results['valueRanges'][0]['values']
    return sheet_values


async def add_new_achievement(date_of_achievement, name_of_achievement, name_of_user, id_in_tg):
    # сверху добавил async и ниже await с слипом и пропала ошибка "object NoneType can't be used in 'await' expression"
    await asyncio.sleep(1)
    last_line = await get_amount_of_achievements()
    results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body={
        "valueInputOption": "USER_ENTERED",
        # Данные воспринимаются, как вводимые пользователем (считается значение формул)
        "data": [
            {"range": f"Ачивки!B{int(last_line) + 1}:E{int(last_line) + 1}",
             "majorDimension": "ROWS",  # Сначала заполнять строки, затем столбцы
             "values": [
                 [f"{date_of_achievement}", f"{name_of_achievement}", f"{name_of_user}", f"{id_in_tg}"]
             ]}
        ]
    }).execute()


async def get_achievements_group_by_date():
    await asyncio.sleep(1)
    achievements_group_by_date = dict() # ключ - дата, значения - список из ачивки, имени пользователя, и даты
    list_of_achievements = await get_list_of_achievements()
    # print(list_of_achievements)
    for list in list_of_achievements:
        date_of_achievement = list[0]
        name_of_user = list[2]
        name_of_achievement = list[1]
        # группируем по дате, внутри создаем словари с пользователями и списком их ачивок за день
        # имя пользователя ключ, список ачивок значение
        if date_of_achievement not in achievements_group_by_date:
            achievements_group_by_date[date_of_achievement] = {name_of_user: [name_of_achievement]}
        else:
            if name_of_user not in achievements_group_by_date[date_of_achievement]:
                achievements_group_by_date[date_of_achievement][name_of_user] = [name_of_achievement]
            else:
                achievements_group_by_date[date_of_achievement][name_of_user].append(name_of_achievement)
    return achievements_group_by_date
    # print(achievements_group_by_date)


async def get_achievements_group_by_user_for_period(amount_of_days=7):
    await asyncio.sleep(1)
    achievements_group_by_user_for_period = dict() # ключ - имя пользователя, значения - список всех ачивок за период
    for date in range(0, amount_of_days):
        try:
            number_of_day = (datetime.today() - timedelta(days=date)).strftime("%d.%m.%Y")
            achievements_by_date = await get_achievements_group_by_date()[number_of_day]
            for key in achievements_by_date:
                if key not in achievements_group_by_user_for_period:
                    achievements_group_by_user_for_period[key] = achievements_by_date[key]
                else:
                    achievements_group_by_user_for_period[key] += achievements_by_date[key]
        except KeyError:
            pass
    return achievements_group_by_user_for_period


# print(group_achievements_by_user_for_period())