import asyncio
from datetime import datetime, timedelta

from aiogram import Bot, types

import main_config
from models import base, db, Money, User
from models.config import Config



async def cmd_stat():
    vbivs = {}
    teachers = {}
    vbivs_uah = {}
    sms_sum = {'pl': 0, 'lt': 0, 'lv': 0, 'sw': 0, 'ro': 0, 'pt': 0, 'pe': 0, 'es': 0, 'tu': 0, 'nl': 0}
    total_sum = 0
    today = datetime.today().replace(minute=0, second=0)
    if today.hour < 4:
        today = today.replace(hour=4) - timedelta(days=0)
    else:
        today = today.replace(hour=4)
    today = today - timedelta(days=1)
    current = (datetime.today() - timedelta(days=0)).replace(hour=4, minute=0, second=0, microsecond=0)
    text = 'Статистика с {} по {}\n'.format(today, current)
    countries = main_config.COUNTRIES
    for c in countries:
        money = await Money.query.where(Money.created > today).where(Money.created < current).where(
            Money.country == countries[c]['country']).gino.all()
        count = 0
        sum = 0
        for m in money:
            if m.teacher_id not in teachers:
                teachers[m.teacher_id] = {c: m.amount * 0.05}
            else:
                if c not in teachers[m.teacher_id]:
                    teachers[m.teacher_id][c] = m.amount * 0.05
                else:
                    teachers[m.teacher_id][c] += m.amount * 0.05
            if m.uid_admin not in vbivs:
                vbivs[m.uid_admin] = {c: m.amount}
            else:
                if c not in vbivs[m.uid_admin]:
                    vbivs[m.uid_admin][c] = m.amount
                else:
                    vbivs[m.uid_admin][c] += m.amount
            if m.uid_admin not in vbivs_uah:
                vbivs_uah[m.uid_admin] = {c: m.uah}
            else:
                if c not in vbivs_uah[m.uid_admin]:
                    vbivs_uah[m.uid_admin][c] = m.uah
                else:
                    vbivs_uah[m.uid_admin][c] += m.uah
            count += 1
            if m.sms:
                sms_sum[countries[c]['country']] += m.amount * 0.1
            sum += m.amount
        text += '<b>{}</b>\n<b>Залетов:</b> {}\n<b>Сумма:</b> {} RUB / {} {}\n\n'.format(c, count,
                                                                                    get_money(countries[c]['country'], sum),
                                                                                    sum, countries[c]['cur'])
        total_sum += get_money(countries[c]['country'], sum)
    text += '\n<b>💰 Итог:</b> {} RUB 💰\n\n👊Вбиверы:\n'.format(int(total_sum))
    for uid in vbivs.keys():
        vbiv = await User.query.where(User.uid == uid).gino.first()
        text += '@{}:\n'.format(vbiv.username)
        for c in vbivs[uid].keys():
            text += f"{c}: {vbivs[uid][c]} | {vbivs_uah[uid][c]} UAH\n"
    text += '👩‍🏫 Наставники:\n'
    for uid in teachers.keys():
        if uid == 0:
            continue
        teacher = await User.query.where(User.uid == uid).gino.first()
        text += '@{}:\n'.format(teacher.username)
        for c in teachers[uid].keys():
            text += f"{c}: {teachers[uid][c]}\n"
    fakes = await Money.query.where(Money.created > today).where(Money.created < current).where(
        Money.fake == True).gino.all()
    fake_text = '\nФейковые залеты:\n'
    if fakes:
        for f in fakes:
            fake_text += f"{f.amount} / {get_money(f.country, f.amount)} rub | {f.country}\n"
    text += '\n\nSMS:\n'
    total_sms_sum = 0
    for c in sms_sum.keys():
        text += f"{c}: {round(sms_sum[c], 2)} / {get_money(c, sms_sum[c])} RUB\n"
        total_sms_sum += get_money(c, sms_sum[c])
    text += 'Итого: {} рублей'.format(total_sms_sum)
    text += fake_text
    return text, int(total_sum)


async def today_report():
    await base.on_startup()
    bot = Bot(main_config.API_TOKEN, parse_mode=types.ParseMode.HTML)
    '''today = datetime.today().replace(minute=0, second=0)
    if today.hour < 4:
        today = today.replace(hour=4) - timedelta(days=1)
    else:
        today = today.replace(hour=4)
    all_users = await db.select([User.hidden_id, db.func.sum(Money.amount)]) \
        .select_from(Money.join(User, onclause=Money.uid_worker == User.uid)) \
        .group_by(User.hidden_id).where(Money.created > today).where(Money.country == 'pl').order_by(db.func.sum(Money.amount).desc()) \
        .limit(10).gino.all()
    if len(all_users) > 0:
        text = '#TOPDAY\n🇵🇱 🔝Топ за сегодня 🇵🇱:\n\n'
        text += '🥇 👨🏻‍💻 <u><b>{}</b></u>: {} RUB / {} PLN\n'.format(all_users[0].hidden_id, get_rub(all_users[0].sum_1), all_users[0].sum_1)
        if len(all_users) > 1:
            text += '🥈 👨🏻‍💻 <u><b>{}</b></u>: {} RUB / {} PLN\n'.format(all_users[1].hidden_id, get_rub(all_users[1].sum_1), all_users[1].sum_1)
        if len(all_users) > 2:
            text += '🥉 👨🏻‍💻 <u><b>{}</b></u>: {} RUB / {} PLN\n'.format(all_users[2].hidden_id, get_rub(all_users[2].sum_1), all_users[2].sum_1)
        max_len = 10 if len(all_users) > 10 else len(all_users)
        if len(all_users) > 3:
            for i in range(3, max_len):
                text += '💰{}. 👨🏻‍💻 <u><b>{}</b></u>: {} RUB / {} PLN\n'.format(i + 1, all_users[i].hidden_id, get_rub(all_users[i].sum_1),
                                                              all_users[i].sum_1)
        total_sum = await db.select([db.func.sum(Money.amount)]).where(Money.created > today).where(Money.country == 'pl').gino.scalar()
        text += '\n<u><b>💸Всего за день: {} RUB / {} PLN💸</b></u>'.format(get_rub(total_sum), total_sum)
        #await bot.send_message(config.PL_LVL2_CHAT, text)
        await asyncio.sleep(1)
        #await bot.send_message(config.PL_LVL1_CHAT, text)'''
    daily_all, total = await cmd_stat()
    await bot.send_message(1411427861, daily_all)
    for a in main_config.ADMIN_IDS:
        try:
            await bot.send_message(a, daily_all)
        except:
            pass
    await bot.close()


def get_rub(PLN):
    return int(round(PLN * 18.5, 0))


def get_byn_rub(byn):
    return round(byn * 28.45, 0)

def get_kzt_rub(mdl):
    return round(mdl * 0.17, 0)

def get_pln_rub(mdl):
    return round(mdl * 18.5, 0)

def get_huf_rub(mdl):
    return round(mdl * 0.20, 0)

def get_uah_rub(uah):
    return round(uah * 2.64, 0)

def get_eur_uah(uah):
    return round(uah * 0.029, 0)

def get_eur_rub(eur):
    return round(eur * 85, 0)

def get_czk_rub(czk):
    return round(czk * 3.50, 0)

def get_gbp_rub(gbp):
    return int(round(gbp * 85, 0))

def get_uah_lei(eur):
    return round(eur * 0.15, 0)


def get_lei_rub(eur):
    return round(eur * 18.22, 0)

def get_aud_rub(eur):
    return round(eur * 54, 0)

def get_kr_rub(eur):
    return round(eur * 8.49, 0)

def get_sol_rub(EUR):
    return round(EUR * 17.74, 0)


def get_tu_rub(EUR):
    return round(EUR * 8.43, 0)

def get_money(country, money):
    if country == 'pl':
        payout_rub = get_pln_rub(money)
    elif country == 'by':
        payout_rub = get_rub(money)
    elif country == 'ro':
        payout_rub = get_lei_rub(money)
    elif country == 'en':
        payout_rub = get_eur_rub(money)
    elif country == 'sw':
        payout_rub = get_kr_rub(money)
    elif country == 'pe':
        payout_rub = get_sol_rub(money)
    else:
        payout_rub = get_eur_rub(money)
    return payout_rub

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(today_report())
