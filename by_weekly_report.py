import asyncio
import datetime

from aiogram import Bot

import main_config
import locale
from models import base, Money, User


async def send_report():
    await base.on_startup()
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
    today = datetime.datetime.today().replace(hour=0, minute=0, second=0)
    today_end = datetime.datetime.today().replace(hour=23, minute=59, second=59)
    bot = Bot(main_config.API_TOKEN)
    text = '🇧🇾 Беларусь 🇧🇾\n💰Статистика за неделю💰\n\n'
    total_sum = 0
    total_pay = 0
    total_count = 0
    for i in range(6, -1, -1):
        print(i)
        d = datetime.timedelta(days=i)
        day_start = today - d
        day_end = today_end - d
        money = await Money.query.where(Money.created > day_start).where(Money.country == 'by').where(Money.created < day_end).gino.all()
        sum = 0
        pay_sum = 0
        count = 0
        for m in money:
            count += 1
            sum += m.amount
            pay_sum += round(m.amount * (m.percent / 100), 0)
        text += '🗓{}:🗓\n'.format(day_start.strftime('%A'))
        text += '🐘Залетов: {}🐘\n💸Заработано: {} RUB / {} BYN💸\n💵Выплачено: {} RUB / {} BYN💵\n\n'\
            .format(count, get_rub(sum), sum, get_rub(pay_sum), pay_sum)
        total_sum += sum
        total_pay += pay_sum
        total_count += count
    text += '🗓Всего:🗓\n' \
        '🐘Залетов: {}🐘\n💸Заработано: {} RUB / {} BYN💸\n💵Выплачено: {} RUB / {} BYN💵\n\n' \
            .format(total_count, get_rub(total_sum), total_sum, get_rub(total_pay), total_pay)
    await bot.send_message(main_config.ERROR_CHANNEL, text)
    await bot.close()


def get_rub(byn):
    return byn * 30


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(send_report())