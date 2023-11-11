import asyncio
import datetime

from aiogram import Bot, types

import main_config
from models import base, User


async def clean_users():
    text = '🔒Вы были неактивны долгое время, поэтому мы удалили вас из бота и чатов.\n' \
           '📝Если вы хотите продолжить работу, свяжитесь с @onegin_01 и уточните причину вашего простоя.'
    await base.on_startup()
    bot = Bot(main_config.API_TOKEN)
    chat_count = await bot.get_chat_members_count(main_config.LVL2_CHAT)
    users = await User.query.where(User.status == True).gino.all()
    count = 0
    counter = 0
    print('chat: {}'.format(chat_count))
    for u in users:
        print('Checked: {} PRO: {}'.format(counter, count))
        is_chat_member = False
        try:
            member = await bot.get_chat_member(main_config.LVL2_CHAT, u.uid)
            if member.status != types.ChatMemberStatus.LEFT:
                is_chat_member = True
        except Exception:
            pass
        if is_chat_member:
            await u.update(pro_access=True).apply()
            count += 1
        await asyncio.sleep(1)
        counter += 1
    await bot.send_message(1303591006, 'Chat count: {}\nChecked count: {}'.format(chat_count, count))
    await bot.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(clean_users())
