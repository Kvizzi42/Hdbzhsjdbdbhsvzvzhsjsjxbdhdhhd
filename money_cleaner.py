import asyncio
import datetime

import pytz
from aiogram import Bot

import main_config
from models import base, User, db, Money, Requests


async def clean_users():
    text = '🔒У тебя нет профитов более месяца, поэтому мы удалили тебя из бота и чатов.\n' \
           '📝Если ты хочешь продолжить работу, подай заявку в бота снова. Либо свяжись с @onegin_01 или @Tinky_Winky159 и уточни причину твоего простоя.'
    results = open('clean_logs.txt', 'w')
    await base.on_startup()
    bot = Bot(main_config.API_TOKEN)
    today = datetime.datetime.today().replace(hour=0, minute=0, second=0, tzinfo=pytz.UTC)
    d = datetime.timedelta(days=30)
    old_date = today - d
    users = await User.query.where(User.status == True).gino.all()
    print('Count: {}'.format(len(users)))
    del_arr = []
    del_uid_arr = []
    del_in_arr = []
    for u in users:
        if u.admin:
            continue
        money = await Money.query.where(Money.uid_worker == u.uid).order_by(Money.created.desc()).gino.first()
        if money:
            if money.created:
                if money.created < old_date:
                    print(f"@{u.username} {money.created}")
                    del_arr.append(u)
                    del_uid_arr.append(u.uid)
        else:
            if u.created:
                if u.created < old_date:
                    del_in_arr.append(u.uid)
    print(f"{len(del_arr)} {len(del_in_arr)}")
    counter = 0
    start_date = datetime.datetime.now()
    success = 0
    fail = 0
    total = len(del_arr)
    chats = [-1001481747209, -1001493934439, -000, -000, -1001283818261, -1001484634516]
    await Requests.delete.where(Requests.uid.in_(del_uid_arr)).gino.status()
    for u in del_arr:
        print('Total: {} / {}'.format(counter, total))
        await u.update(status=False).apply()
        try:
            await bot.send_message(u.uid, text)
            results.write('{} заблокирован. Уведомление отправлено.\n'.format(u.uid))
            success += 1
        except Exception as e:
            results.write('{}. Бот заблокирован\n'.format(u.uid))
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
