# статья с описанием работы - https://habr.com/ru/post/483302/

# Подключаем библиотеки
import asyncio

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = 'data/google_sheet_auth.json'  # Имя файла с закрытым ключом, вы должны подставить свое

# Читаем ключи из файла
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http()) # Авторизуемся в системе
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth) # Выбираем работу с таблицами и 4 версию API

# spreadsheet = service.spreadsheets().create(body = {
#     'properties': {'title': 'Первый тестовый документ', 'locale': 'ru_RU'},
#     'sheets': [{'properties': {'sheetType': 'GRID',
#                                'sheetId': 0,
#                                'title': 'Лист номер один',
#                                'gridProperties': {'rowCount': 100, 'columnCount': 15}}}]
# }).execute()
spreadsheetId = '1pxrkIrlNgUnhTK1jj00iYxu5jlpl79nEy77yvntckvo' #spreadsheet['spreadsheetId'] # сохраняем идентификатор файла
print('https://docs.google.com/spreadsheets/d/' + spreadsheetId)
#
driveService = apiclient.discovery.build('drive', 'v3', http = httpAuth) # Выбираем работу с Google Drive и 3 версию API
access = driveService.permissions().create(
    fileId = spreadsheetId,
    body = {'type': 'user', 'role': 'writer', 'emailAddress': 'mozzgishere@gmail.com'},  # Открываем доступ на редактирование
    fields = 'id'
).execute()
#
# # Добавление листа
# results = service.spreadsheets().batchUpdate(
#     spreadsheetId=spreadsheetId,
#     body=
#     {
#         "requests": [
#             {
#                 "addSheet": {
#                     "properties": {
#                         "title": "Еще один лист",
#                         "gridProperties": {
#                             "rowCount": 20,
#                             "columnCount": 12
#                         }
#                     }
#                 }
#             }
#         ]
#     }).execute()
#
# # Получаем список листов, их Id и название
spreadsheet = service.spreadsheets().get(spreadsheetId=spreadsheetId).execute()
sheetList = spreadsheet.get('sheets')
# for sheet in sheetList:
#     print(sheet['properties']['sheetId'], sheet['properties']['title'])
#
sheetId = sheetList[0]['properties']['sheetId']
#
# print('Мы будем использовать лист с Id = ', sheetId)

async def add_in_achive(date, name_of_ach, name_of_user):
    ### сверху добавил async и ниже await с слипом и пропала ошибка "object NoneType can't be used in 'await' expression"
    await asyncio.sleep(1)
    results = service.spreadsheets().values().batchUpdate(spreadsheetId = spreadsheetId, body = {
        "valueInputOption": "USER_ENTERED", # Данные воспринимаются, как вводимые пользователем (считается значение формул)
        "data": [
            {"range": "Лист номер один!B2:D5",
             "majorDimension": "ROWS",     # Сначала заполнять строки, затем столбцы
             "values": [
                        [f"{date}", f"{name_of_ach}", f"{name_of_user}"], # Заполняем первую строку
                        #['25', "=6*6", "=sin(3,14/2)"]  # Заполняем вторую строку
                   ]}
    ]
    }).execute()


