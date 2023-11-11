import asyncio
import datetime

from aiogram import Bot

import main_config
from models import base
from models import *
from models.leboncoin import Leboncoin


async def clean_links():
    await base.on_startup()
    tables = [Auto2, Avito2, Avito, Bazos, Sbazar, Sdek, Sdek2, Kzsdek, Kzsdek2, Belpost2, Belpost, Dhl, Dhl2, Dpd,
              Dpd2, Ltdpd, Lvdpd, Evro2, Info, Info2, Inpost2, PlOlx2, Plpost2, Kazpost2, Kazpost, Nedvig, Nedvig2,
              Md, Md2, Jof, Lvom, Ltom, Gumtree, Ctt, PtOlx2, Leboncoin, Swblock, Swpost, Allegro, Plbook, Ukbook]

    three_days = datetime.datetime.now().replace(hour=0, microsecond=0, minute=0, second=0) - datetime.timedelta(days=3)
    result = 'Cleaner:\n'
    for t in tables:
        result += '{} deleted {}\n'.format(t.__tablename__, await t.delete.where((t.created < three_days)
                                                                                 & (t.uid != main_config.ERROR_CHANNEL)).gino.status())
    result += '{} deleted {}\n'.format('chat', await Chat.delete.where(Chat.date < three_days.timestamp()).gino.status())
    bot = Bot(main_config.API_TOKEN)
    await bot.send_message(main_config.ERROR_CHANNEL, result)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(clean_links())