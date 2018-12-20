import os
import requests

token = os.getenv('TELE_TOKEN')
method = 'getUpdates'

# url = "https://api.telegram.org/bot{}/{}".format(token,method)
url = "https://api.hphk.io/telegram/bot{}/getUpdates".format(token)
print(url)
res = requests.get(url).json()

user_id = (res["result"][0]["message"]["from"]["id"])
msg = "야"

method = 'sendmessage'
msg_url = msg_url = "https://api.hphk.io/telegram/bot{}/{}?chat_id={}&text={}".format(token,method,user_id,msg)
print(msg_url)
requests.get(msg_url)