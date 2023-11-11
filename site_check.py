import asyncio
import json
import os
import sys

import requests
from aiogram import Bot, types
from requests.exceptions import ProxyError


async def send_tg(text, settings: dict):
    bot = Bot(token='954720646:AAEkt0dh1pDmgB5Z6BEvezU508Er5FRARSg', parse_mode=types.ParseMode.HTML)
    if len(settings['messages']) > 0:
        for msg in settings['messages']:
            await bot.delete_message(msg['chat_id'], msg['message_id'])
        await asyncio.sleep(0.5)
    messages = []
    for chat_id in settings['chats']:
        msg = await bot.send_message(chat_id, text, disable_web_page_preview=True)
        messages.append({'chat_id': chat_id, 'message_id': msg.message_id})
        await asyncio.sleep(0.5)
    settings['messages'] = messages
    json.dump(settings, open('settings.json', 'w'))

os.chdir(sys.path[0])
proxy = {'http': 'http://aP7oJJ:qXoD1b@212.102.150.185:8000/', 'https': 'http://aP7oJJ:qXoD1b@212.102.150.185:8000/'}
sdek = "https://sdek.be"
belpost = "https://belpost.io"
kufarin = "https://kufar.co"
kufarbiz = "https://kufar.co"
s = requests.Session()
result = 'Статус сайтов:\n'
active = 'Активен ✅ '
inactive = 'Неактивен ❌'
settings = json.load(open('settings.json'))
try:
    res = s.get(sdek, proxies=proxy)
    if res.status_code == 200:
        settings['sdek'] = '💎Sdek: <b>' + active + '</b>'
    else:
        settings['sdek'] = '💎Sdek: <b>' + inactive + '</b>'
except ProxyError:
    print('Proxy error for sdek')
    settings['sdek'] = '💎Sdek: <b>' + inactive + '</b>'
try:
    res = s.get(belpost, proxies=proxy)
    if res.status_code == 200:
        settings['belpost'] = '💎Belpost: <b>' + active + '</b>'
    else:
        settings['belpost'] = '💎Belpost: <b>' + inactive + '</b>'
except ProxyError:
    print('Proxy error for belpost')
    settings['belpost'] = '💎Belpost: <b>' + inactive + '</b>'

try:
    res = s.get(kufarbiz, proxies=proxy)
    if res.status_code == 200:
        settings['kufar2'] = '💎Kufar 2.0: <b>' + active + '</b>'
    else:
        settings['kufar2'] = '💎Kufar 2.0: <b>' + inactive + '</b>'
except ProxyError:
    print('Proxy error for kufar2')
    settings['kufar2'] = '💎Kufar 2.0: <b>' + inactive + '</b>'

try:
    res = s.get(kufarin, proxies=proxy)
    if res.status_code == 200:
        settings['kufar'] = '💎Kufar 1.0: <b>' + active + '</b>'
    else:
        settings['kufar'] = '💎Kufar 1.0: <b>' + inactive + '</b>'
except ProxyError:
    print('Proxy error for kufar1')
    settings['kufar'] = '💎Kufar 1.0: <b>' + inactive + '</b>'
json.dump(settings, open('settings.json', 'w'))