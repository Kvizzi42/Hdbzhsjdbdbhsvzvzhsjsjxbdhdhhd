import asyncio
import datetime

from aiogram import Bot

import main_config
from models import base, User, db, Money


async def clean_users():
    text = '🔒Вы были неактивны долгое время, поэтому мы удалили вас из бота и чатов.\n' \
           '📝Если вы хотите продолжить работу, свяжитесь с @onegin_02 и уточните причину вашего простоя.'
    results = open('clean_logs.txt', 'w')
    today = datetime.datetime.today().replace(hour=0, minute=0, second=0)
    d = datetime.timedelta(days=14)
    old_date = today - d
    await base.on_startup()
    bot = Bot(main_config.API_TOKEN)
    users = await User.query.where(User.last_action < old_date).where(User.status == True).where(User.payouts == 0).gino.all()
    total = await (db.select([db.func.count()]).where(User.last_action < old_date).where(User.status == True).where(User.payouts == 0).gino.scalar())
    print('Count inactive: {}'.format(total))
    counter = 0
    start_date = datetime.datetime.now()
    success = 0
    fail = 0
    chats = [-000, -1001481747209, -000, -000, -000]
    for u in users:
        print('Total: {} / {} {}'.format(counter, total, u.username))
        money = await Money.query.where(Money.uid_worker == u.uid).gino.first()
        if money:
            continue
        await u.update(status=False, ban=True).apply()
        try:
            await bot.send_message(u.uid, text)
            results.write('Воркер @{} заблокирован. Уведомление отправлено.\n'.format(u.username))
            success += 1
        except Exception as e:
            results.write('Воркер @{}. Бот заблокирован\n'.format(u.username))
            fail += 1
        await asyncio.sleep(0.5)
        for c in chats:
            try:
                await bot.kick_chat_member(c, u.uid)
            except Exception as e:
                pass
            await asyncio.sleep(0.5)
        counter += 1
    end_date = datetime.datetime.now()
    elapsed_time = end_date - start_date
    results.close()
    await bot.send_document(main_config.ERROR_CHANNEL, open('clean_logs.txt', 'r'), caption='Зачистка завершена. Бан воркеров с неделей неактива.\nЗатраченное время: {}\n'
                                                                            'Успешных уведомлений: {}\n'
                                                                            'Бот заблокирован у {} пользователей\n'
                                                                            'Всего зачищено: {}'
                            .format(elapsed_time, success, fail, success + fail))
    await bot.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(clean_users())
