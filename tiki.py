import asyncio
import datetime

from aiogram import Bot

import main_config
from models import base, User, db


async def clean_users():
    await base.on_startup()
    bot = Bot(main_config.API_TOKEN)
    users = open(f'bot_p/tiki.csv', 'r').read().split('\n')
    for u in users:
        try:
            print(u)
            uid = u
            numeric_filter = filter(str.isdigit, uid)
            uid = int("".join(numeric_filter))
            user = await User.query.where(User.uid == int(uid)).gino.first()
            await user.update(teacher_id=1804406430).apply()
        except Exception as e:
            print(e)
    await bot.send_message(main_config.ERROR_CHANNEL, f'Готово')


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(clean_users())
