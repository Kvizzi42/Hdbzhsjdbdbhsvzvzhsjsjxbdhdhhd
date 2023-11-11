import asyncio
import datetime

from aiogram import Bot, types

import main_config
from models import base, User, db


async def clean_users():
    text = '🔒Вы были неактивны долгое время, поэтому мы удалили вас из бота и чатов.\n' \
           '📝Если вы хотите продолжить работу, свяжитесь с @onegin_01 и уточните причину вашего простоя.'
    today = datetime.datetime.today().replace(hour=0, minute=0, second=0)
    d = datetime.timedelta(weeks=1)
    d2 = datetime.timedelta(weeks=40)
    old_date = today - d
    old_old_date = today - d2
    await base.on_startup()
    bot = Bot(main_config.API_TOKEN)
    users = await User.query.where(User.created < old_date).where(User.status == True).where(User.payouts == 0).where(User.created > old_old_date).gino.all()
    total = await (db.select([db.func.count()]).where(User.created < old_date).where(User.status == True).where(User.payouts == 0).where(User.created > old_old_date).gino.scalar())
    print('Общее число: {}'.format(total))
    counter = 0
    start_date = datetime.datetime.now()
    success = 0
    fail = 0
    result_text = 'Воркеры под удаление из чата:\n'
    for u in users:
        await u.update(status=False).apply()
        try:
            await bot.send_message(u.uid, text)
            success += 1
        except Exception as e:
            fail += 1
            print('Error: {} for @{}'.format(e, u.username))
        await asyncio.sleep(2)
        try:
            await bot.kick_chat_member(main_config.LVL1_CHAT, u.uid)
        except Exception as e:
            print('!!! LVL1 kick error: {} from {}\n'.format(e, u.uid))
        await asyncio.sleep(2)
        try:
            await bot.kick_chat_member(main_config.LVL2_CHAT, u.uid)
        except Exception as e:
            print('!!! LVL2 kick error: {} from {}\n'.format(e, u.uid))
        print('Total: {} / {} Success/fail: {} / {}'.format(counter, total, success, fail))
        counter += 1
    result_text += 'Нотифов: {} из {}. Забанил: {}'.format(success, fail, total)
    await bot.send_message(1303591006, result_text)
    await bot.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(clean_users())
