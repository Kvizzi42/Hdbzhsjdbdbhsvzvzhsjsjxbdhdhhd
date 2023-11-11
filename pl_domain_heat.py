import asyncio
import datetime

import aiohttp
import requests
from aiogram import Bot

import main_config
from models import base
from models import *


async def check_domains():
    await base.on_startup()
    timeout = aiohttp.ClientTimeout(total=10)
    s = aiohttp.ClientSession(timeout=timeout)
    bot = Bot(main_config.API_TOKEN)
    domains = await DomainOrder.query.where((DomainOrder.heat == False) & (DomainOrder.domain.contains('pl'))).gino.all()
    s = aiohttp.ClientSession()
    heat_count = await (db.select([db.func.count()]).where((DomainOrder.used == False) & (DomainOrder.heat == True) & (
        DomainOrder.domain.startswith('pl-'))).gino.scalar())
    doms = ['olx', 'inpost', 'allegro', 'sms', 'vinted', 'poczta']
    for d in domains:
        try:
            error = False
            for name in doms:
                try:
                    full_name = 'https://{}.{}'.format(name, d.domain)
                    await s.get(full_name)
                    print(f"{full_name} OK")
                except:
                    full_name = 'https://{}.{}'.format(name, d.domain)
                    error = True
                    print(f"{full_name} ERROR")
            if error:
                continue
            await d.update(heat=True).apply()
            heat_count += 1
            await bot.send_message(-000, 'Новый домен готов к работе. Прогретых в запасе {}'.format(heat_count))
        except Exception as e:
            print(f"{d.domain} {e}")
    await s.close()
    await bot.close()
    

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(check_domains())