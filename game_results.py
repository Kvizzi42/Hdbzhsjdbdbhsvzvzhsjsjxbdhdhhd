import asyncio
import datetime

from aiogram import Bot, types

import main_config
from models import base, db, Money, User


async def today_report():
    await base.on_startup()
    bot = Bot(main_config.API_TOKEN, parse_mode=types.ParseMode.HTML)
    today = datetime.datetime.today().replace(hour=0, minute=0, second=0)
    old_date = today - datetime.timedelta(days=today.weekday())
    users = await db.select([User.username, db.func.sum(Money.amount), User.uid]) \
        .select_from(Money.join(User, onclause=Money.uid_worker == User.uid)) \
        .group_by(User.username).group_by(User.uid).where(Money.created > old_date).order_by(db.func.sum(Money.amount).desc()) \
        .limit(5).gino.all()
    total_sum = 0
    personal_text = '🥳 Поздравляем с занятым {} местом!!! 🤩 \n Чтобы получить приз, отпиши любому из админов (/adm) 🤙🏻'
    if len(users) > 0:
        text = '<b>🎩 Результаты еженедельного конкурса: </b>\n\n'
        total_sum += users[0].sum_1
        text += '🥇 <a href="t.me/{}">{}</a>: {} BYN\n'.format(users[0].username, users[0].username, users[0].sum_1)
        await bot.send_message(users[0].uid, personal_text.format('🥇 1'))
        await asyncio.sleep(.3)
        if len(users) > 1:
            total_sum += users[1].sum_1
            text += '🥈 <a href="t.me/{}">{}</a>: {} BYN\n'.format(users[1].username, users[1].username, users[1].sum_1)
            await bot.send_message(users[1].uid, personal_text.format('🥈 2'))
            await asyncio.sleep(.3)
        if len(users) > 2:
            total_sum += users[2].sum_1
            text += '🥉 <a href="t.me/{}">{}</a>: {} BYN\n'.format(users[2].username, users[2].username, users[2].sum_1)
            await bot.send_message(users[2].uid, personal_text.format('🥉 3'))
            await asyncio.sleep(.3)
        if len(users) > 3:
            for i in range(3, len(users)):
                total_sum += users[i].sum_1
                text += '💰{}. <a href="t.me/{}">{}</a>: {} BYN\n'.format(i + 1, users[i].username, users[i].username, users[i].sum_1)
                await bot.send_message(users[i].uid, personal_text.format(f'🎖 {i+1}'))
                await asyncio.sleep(.3)
        text += '\n🥳 Поздравляем победителей! 🤩\n\nУсловия еженедельного конкурса, призы и другую информацию ' \
                '<a href="https://t.me/winky_money/716">можно прочитать в этом посте</a>'
        await bot.send_sticker(main_config.LVL1_CHAT, 'CAACAgIAAxkBAAEGW11fnuHONGu6-t7AfFP9YPee_rf2WwACjwoAAhDZCEriSeW2QBmCgx4E')
        await bot.send_message(main_config.LVL1_CHAT, text, disable_web_page_preview=True)
        await asyncio.sleep(1)
        await bot.send_sticker(main_config.LVL2_CHAT,
                               'CAACAgIAAxkBAAEGW11fnuHONGu6-t7AfFP9YPee_rf2WwACjwoAAhDZCEriSeW2QBmCgx4E')
        await bot.send_message(main_config.LVL2_CHAT, text, disable_web_page_preview=True)
    await bot.close()


def get_rub(byn):
    return round(byn * 30, 0)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(today_report())
