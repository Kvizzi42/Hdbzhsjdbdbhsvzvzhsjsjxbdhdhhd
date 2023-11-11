import asyncio
import datetime

from aiogram import Bot

import main_config
from models import base, User, Money


async def clean_users():
    text = '🔒Сумма занесенных профитов менее 700 BYN, поэтому мы удалили вас из PRO чата.'
    await base.on_startup()
    bot = Bot(main_config.API_TOKEN)
    success = 0
    fail = 0
    for_kick = {}
    today = datetime.datetime.today().replace(hour=0, minute=0, second=0, tzinfo=None)
    d = datetime.timedelta(days=10)
    d1 = datetime.timedelta(weeks=4)
    old_date = today - d
    old_date = old_date.replace(tzinfo=datetime.timezone.utc)
    old_date1 = today - d1
    old_date1 = old_date1.replace(tzinfo=datetime.timezone.utc)
    import logging
    logging.basicConfig(level=logging.DEBUG)
    users = await User.query.where(User.status == True).where(User.created < old_date)\
        .where(User.created > old_date1).where(User.pro_access == False).gino.all()
    for u in users:
        m = await Money.query.where(Money.uid_worker == u.uid).order_by(Money.created.desc()).gino.first()
        if m:
            for_kick[u.username] = m.created
        else:
            for_kick[u.username] = None
        print(u.created)
    today = datetime.datetime.today().replace(hour=0, minute=0, second=0, tzinfo=datetime.timezone.utc, day=10)
    for k in for_kick.keys():
        if for_kick[k]:
            if for_kick[k] < today:
                pass
                #print('@{} {}'.format(k, for_kick[k]))
    #print('Total count: {}'.format(len(for_kick)))
    return
    today = datetime.datetime.today().replace(hour=0, minute=0, second=0, tzinfo=None)
    d = datetime.timedelta(weeks=3)
    old_date = today - d
    old_date = old_date.replace(tzinfo=datetime.timezone.utc)
    workers = []
    for u in workers:
        try:
            await bot.kick_chat_member(main_config.LVL2_CHAT, u)
            print('User kicked lvl2 for {}\n'.format(u))
        except Exception as e:
            print('!!! LVL2 kick error: {} from {}\n'.format(e, u))
        await asyncio.sleep(1)
    await bot.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(clean_users())