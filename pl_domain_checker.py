import asyncio
import datetime

import aiohttp
from aiogram import Bot

import main_config
from models import base
from models import *


async def check_domains():
    await base.on_startup()
    bot = Bot(main_config.API_TOKEN)
    domains = await DomainOrder.query.where(DomainOrder.blacklist == False).gino.all()
    s = aiohttp.ClientSession()
    resp = await (await s.get('http://hole.cert.pl/domains/domains.txt')).text()
    data = resp.split('\n')
    blacklist = []
    for d in data:
        d = d.split('.')
        try:
            blacklist.append(f"{d[1]}.{d[2]}")
        except Exception:
            pass
    for d in domains:
        print(d.domain)
        if d.domain in blacklist:
            await d.update(blacklist=True).apply()
            await bot.send_message(main_config.ERROR_CHANNEL, 'Домен {} попал в блеклист'.format(d.domain))
    await s.close()
    

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(check_domains())