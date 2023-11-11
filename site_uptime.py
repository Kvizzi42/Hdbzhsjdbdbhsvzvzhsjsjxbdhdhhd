import asyncio
from datetime import datetime

from aiogram import Bot, types
from aiogram.utils.exceptions import MessageNotModified, MessageToEditNotFound
import requests, main_config
from models import base, Uptime


async def check_sites():
    await base.on_startup()
    kufar = main_config.HOSTNAME_KUFAR
    sdek = main_config.HOSTNAME_SDEK
    belpost = main_config.HOSTNAME_BELPOST
    evro = main_config.HOSTNAME_EVRO
    https_proxy = "https://gSLXfZvglT:VYsZgaJwbe@45.138.159.71:55239"
    proxyDict = {
        "https": https_proxy
    }
    try:
        res = requests.get(kufar, proxies=proxyDict)
        if res.status_code == 200:
            is_kufar = True
        else:
            is_kufar = False
    except Exception as e:
        is_kufar = False
        print(e)
    try:
        res = requests.get(sdek, proxies=proxyDict)
        if res.status_code == 200:
            is_sdek = True
        else:
            is_sdek = False
    except Exception as e:
        is_sdek = False
        print(e)
    try:
        res = requests.get(belpost, proxies=proxyDict)
        if res.status_code == 200:
            is_belpost = True
        else:
            is_belpost = False
    except Exception as e:
        is_belpost = False
        print(e)
    try:
        res = requests.get(evro, proxies=proxyDict)
        if res.status_code == 200:
            is_evro = True
        else:
            is_evro = False
    except Exception as e:
        is_evro = False
        print(e)
    await Uptime.create(kufar=is_kufar, sdek=is_sdek, belpost=is_belpost, evro=is_evro, checked=datetime.now())


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(check_sites())
