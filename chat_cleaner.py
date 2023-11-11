import asyncio
import datetime

from aiogram import Bot

import main_config
from models import base, User, db


async def clean_users():
    country = 'users'
    users = open(f'bot_p/{country}.txt', 'r').read().split('\n')
    #users = ['000']
    chat = -1001493934439
    await base.on_startup()
    bot = Bot(main_config.API_TOKEN)
    count = 0
    check = 0
    total = len(users)
    for u in users:
        if u == '':
            continue
        user = await User.query.where(User.uid == int(u)).gino.first()
        check += 1
        if user:
            if user.status:
                continue
        try:
            await bot.kick_chat_member(chat, u)
        except Exception as e:
            print(f"{u} {e}")
        count += 1
        await asyncio.sleep(.50)
        print(f"{check} / {total}")
    await bot.send_message(main_config.ERROR_CHANNEL, f'Чат {country} очищено {count}')


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(clean_users())
