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
    bot = Bot(main_config.API_TOKEN, parse_mode=types.ParseMode.HTML)
    users = await db.select([User.uid, User.username, db.func.sum(Money.amount)]) \
        .select_from(Money.join(User, onclause=Money.uid_worker == User.uid)) \
        .where(Money.country == 'en').group_by(User.username, User.uid).order_by(db.func.sum(Money.amount).desc()) \
        .gino.all()
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



if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(today_report())
