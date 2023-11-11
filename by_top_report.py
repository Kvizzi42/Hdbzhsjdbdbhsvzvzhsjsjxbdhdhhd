import asyncio
from datetime import datetime

from aiogram import Bot, types

import main_config
from models import base, db, Money, User


async def today_report():
    await base.on_startup()
    bot = Bot(main_config.API_TOKEN, parse_mode=types.ParseMode.HTML)
    today = datetime.today().replace(hour=0, minute=0, second=0)
    all_users = await db.select([User.hidden_id, db.func.sum(Money.amount)]) \
        .select_from(Money.join(User, onclause=Money.uid_worker == User.uid)) \
        .group_by(User.hidden_id).where(Money.created > today).where(Money.country == 'by').order_by(db.func.sum(Money.amount).desc()) \
        .limit(10).gino.all()
    if len(all_users) > 0:
        text = '#TOPDAY\n🇧🇾 🔝Топ за сегодня 🇧🇾:\n\n'
        text += '🥇 👨🏻‍💻 <u><b>{}</b></u>: {} RUB / {} BYN\n'.format(all_users[0].hidden_id, get_rub(all_users[0].sum_1), all_users[0].sum_1)
        if len(all_users) > 1:
            text += '🥈 👨🏻‍💻 <u><b>{}</b></u>: {} RUB / {} BYN\n'.format(all_users[1].hidden_id, get_rub(all_users[1].sum_1), all_users[1].sum_1)
        if len(all_users) > 2:
            text += '🥉 👨🏻‍💻 <u><b>{}</b></u>: {} RUB / {} BYN\n'.format(all_users[2].hidden_id, get_rub(all_users[2].sum_1), all_users[2].sum_1)
        max_len = 10 if len(all_users) > 10 else len(all_users)
        if len(all_users) > 3:
            for i in range(3, max_len):
                text += '💰{}. 👨🏻‍💻 <u><b>{}</b></u>: {} RUB / {} BYN\n'.format(i + 1, all_users[i].hidden_id, get_rub(all_users[i].sum_1),
                                                              all_users[i].sum_1)
        total_sum = await db.select([db.func.sum(Money.amount)]).where(Money.created > today).where(Money.country == 'by').gino.scalar()
        text += '\n<u><b>💸Всего за день: {} RUB / {} BYN💸</b></u>'.format(get_rub(total_sum), total_sum)
        await bot.send_message(main_config.LVL2_CHAT, text)
        await asyncio.sleep(1)
        await bot.send_message(main_config.LVL1_CHAT, text)
    await bot.close()


def get_rub(BYN):
    return int(round(BYN * 29.51, 0))


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(today_report())
