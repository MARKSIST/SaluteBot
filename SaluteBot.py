# Бот с помощью getUpdates получает последнее обновление и приветствует или прощается с пользователем
import requests
from config import TOKEN, CHAT_ID

url_updates = (f'https://api.telegram.org/bot{TOKEN}/getUpdates')
url_msg = (
    f'https://api.telegram.org/bot{TOKEN}/sendMessage?CHAT_ID={CHAT_ID}&parse_mode=Markdown&text=')

response = requests.get(url_updates)
res = response.json()['result']
update_id = response.json()['result'][len(res)-1]['update_id']
last_message = response.json()['result'][len(res)-1]['message']

if 'new_chat_member' in last_message.keys():
    new_chat_member = last_message.get('new_chat_member')
    first_name = new_chat_member.get('first_name')
    msg = (f'Привет {first_name}')
    response = requests.get(url_msg + msg)
elif 'left_chat_member' in last_message.keys():
    left_chat_member = last_message.get('left_chat_member')
    first_name = left_chat_member.get('first_name')
    msg = (f'Пока {first_name}')
    response = requests.get(url_msg + msg)
else:
    print('nothing')

# clear history action
response = requests.get(url_updates+'?offset='+str(update_id))
