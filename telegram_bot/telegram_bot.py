import requests
import pprint


TOKEN = 'YOUR_TOKEN'

MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'

#Инофрмация о боте
url = f'{MAIN_URL}/getME'

result = requests.get(url)

#print(result.json())

#pprint.pprint(result.json())


#Получение обновления
url = f'{MAIN_URL}/getUpdates'

result = requests.get(url)

pprint.pprint(result.json())


messages = result.json()['result']

for message in messages:
    #Как ответить на сообщения
    chat_id = message['message']['chat']['id']
    url = f'{MAIN_URL}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': 'SallamAleikum!'
    }

result = requests.get(url, params=params)
pprint.pprint(result.json())