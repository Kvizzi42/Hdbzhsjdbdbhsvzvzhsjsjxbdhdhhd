import asyncio
import datetime

from aiogram import Bot, types

import main_config
from models import base, User, db


async def clean_users():
    text = '🔒Вы были неактивны долгое время, поэтому мы удалили вас из бота и чатов.\n' \
           '📝Если вы хотите продолжить работу, свяжитесь с @onegin_01 и уточните причину вашего простоя.'
    await base.on_startup()
    bot = Bot(main_config.API_TOKEN)
    total = await db.func.count(User.id).gino.scalar()
    users = await User.query.gino.all()
    count = 0
    banned = 0
    unbanned = 0
    errors = 0
    for u in users:
        print('Total: {} / {}. Banned: {} Not banned: {} Errors: {}'.format(count, total, banned, unbanned, errors))
        is_chat_member = False
        try:
            member = await bot.get_chat_member(main_config.LVL2_CHAT, u.uid)
            if member.status != types.ChatMemberStatus.LEFT:
                is_chat_member = True
            if not is_chat_member:
                await asyncio.sleep(1)
                member = await bot.get_chat_member(main_config.LVL1_CHAT, u.uid)
                if member.status != types.ChatMemberStatus.LEFT:
                    is_chat_member = True
        except Exception:
            pass
        if not is_chat_member:
            try:
                await bot.kick_chat_member(main_config.MONEY_CHANNEL[0], u.uid)
                banned += 1
            except Exception as e:
                print('Error {} for: {} {}'.format(e, u.username or u.uid, u.uid))
                errors += 1
        else:
            unbanned += 1
        count += 1
        await asyncio.sleep(1)
    await bot.send_message(1303591006, 'Всего: {} / {}. Забанил: {} Не забанил: {} Бот забанен / воркер удален: {}'
                           .format(count, total, banned, unbanned, errors))
    await bot.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(clean_users())