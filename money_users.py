import asyncio
from datetime import datetime

from aiogram import Bot, types

import main_config
from models import base, db, Money, User


async def is_en_lvl2_member(uid, bot: Bot):
    try:
        member = await bot.get_chat_member(main_config.EN_LVL2_CHAT, uid)
        if member:
            if member.status != 'left' and member.status != 'kicked':
                return True
        return False
    except Exception as e:
        return False


async def today_report():
    await base.on_startup()
    file = open('uids.txt', 'r')
    text = file.read().split('\n')
    out = open('result.txt', 'w')
    for i in range(len(text)):
        text[i] = int(text[i])
    countries = ['pl', 'en', 'by', 'lt', 'lv', 'es', 'pt']
    totals = {}
    for c in countries:
        users = await db.select([User.uid, User.username, db.func.sum(Money.amount)]) \
            .select_from(Money.join(User, onclause=Money.uid_worker == User.uid)) \
            .where(Money.country == c).where(Money.uid_worker.in_(text)).group_by(User.username, User.uid).order_by(db.func.sum(Money.amount).desc()) \
            .gino.all()
        for u in users:
            if u.uid in totals:
                totals[u.uid] += get_money(c, u.sum_1)
            else:
                totals[u.uid] = get_money(c, u.sum_1)
    for k in totals.keys():
        out.write(f"{k} {totals[k]} RUB\n")
    return
    count = 0
    pro_text = '''🏴󠁧󠁢󠁥󠁮󠁧󠁿 Доступ в PRO открыт 🏴󠁧󠁢󠁥󠁮󠁧󠁿
👨🏻‍💻 И тебе одобрен доступ к ней!
🤑 Вперед ебать Англию!!!'''
    kb = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton('💸 Вступить 💸', url='https://t.me/joinchat/3OhR84RYoK1lNDdi'))
    for u in users:
        if not await is_en_lvl2_member(u.uid, bot):
            if u.sum_1 > 0:
                count += 1
                try:
                    await bot.send_sticker(u.uid,
                                       'CAACAgIAAxkBAAEGW11fnuHONGu6-t7AfFP9YPee_rf2WwACjwoAAhDZCEriSeW2QBmCgx4E')
                    await bot.send_message(u.uid, pro_text, reply_markup=kb)
                except Exception as e:
                    print('Er: {} UID: {}'.format(e, u.uid))
            await asyncio.sleep(1)
    await bot.send_message(main_config.ERROR_CHANNEL, 'Приглашено: {}'.format(count))
    await bot.close()


def get_pln_uah(kzt):
    return round(kzt * 0.13, 0)


def get_czk_rub(czk):
    return int(round(czk * 3.50, 0))


def get_gbp_rub(gbp):
    return int(round(gbp * 85, 0))


def get_pln_rub(kzt):
    return round(kzt * 18.5, 0)


def get_eur_uah(uah):
    return round(uah * 0.029, 0)


def get_eur_rub(eur):
    return round(eur * 85, 0)


def get_rub(byn):
    return round(byn * 29, 0)


def get_money(country, money):
    if country == 'pl':
        payout_rub = get_pln_rub(money)
        currency = 'PLN'
    elif country == 'by':
        payout_rub = get_rub(money)
        currency = 'BYN'
    elif country == 'en':
        payout_rub = get_eur_rub(money)
        currency = 'EUR'
    else:
        payout_rub = get_eur_rub(money)
        currency = 'EUR'
    return payout_rub


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(today_report())


