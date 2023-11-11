import asyncio

from aiogram import Bot, types
from aiogram.utils.exceptions import MessageNotModified, MessageToEditNotFound
import main_config
from models import base, db, MoneyNotifies, Money, User


async def check_notifies():
    errors = 'Список ошибок с выплатами:\n'
    is_errors = False
    await base.on_startup()
    bot = Bot(main_config.API_TOKEN, parse_mode=types.ParseMode.HTML)
    notifies = await db.select([Money.amount, Money.percent, Money.uid_worker, MoneyNotifies.message_id, Money.payed,
                                MoneyNotifies.channel_id, MoneyNotifies.edited, MoneyNotifies.id]) \
        .select_from(MoneyNotifies.join(Money, onclause=MoneyNotifies.money_id == Money.id)) \
        .where(MoneyNotifies.edited == False).where(Money.country == 'cz').gino.all()
    for n in notifies:
        print(n.uid_worker)
        try:
            if n.payed:
                amount = round(n.amount * (n.percent / 100), 0)
                worker = await User.query.where(User.uid == n.uid_worker).gino.first()
                try:
                    if worker.anon:
                        user_text = '🌚ID: {}'.format(worker.hidden_id)
                    else:
                        user_text = '👩🏼‍💻Работник: @{}'.format(
                            worker.username)
                    text = '🇨🇿 Чехия\n' \
                           '✅Сумма: {} RUB / {} CZK✅ \n' \
                           '💵Статус: [Оплачено]💵\n' \
                           '📊Процент работника: {}%\n' \
                           '{}'.format(get_rub(n.amount), n.amount, round(n.percent, 0),
                                                        user_text)
                    await bot.edit_message_text(text, n.channel_id, n.message_id)
                except (MessageNotModified, MessageToEditNotFound) as e:
                    print(e)
                await asyncio.sleep(.45)
                try:
                    await bot.send_message(worker.uid, '✅Сумма: {}✅ \n💵 Статус: [Оплачено]💵\n'
                                                       '<b>Внимание:</b> курс CZK к рублю является условным '
                                                       'и статичным, сугубо для ориентирования. '
                                                       'Выплата производится по актуальному курсу.'.format(amount))
                    pass
                except Exception as e:
                    print(e)
                await asyncio.sleep(.45)
                new_payouts = worker.payouts + 1
                await worker.update(payouts=new_payouts).apply()
                is_chat_member = False
                try:
                    member = await bot.get_chat_member(main_config.PL_LVL2_CHAT, worker.uid)
                    if member.status != types.ChatMemberStatus.LEFT:
                        is_chat_member = True
                except Exception:
                    pass
                if not is_chat_member:
                    money = await Money.query.where(Money.uid_worker == worker.uid).where(Money.country == 'cz').gino.all()
                    total_sum = 0
                    for m in money:
                        total_sum += m.amount
                    if total_sum >= 5000:
                        await bot.send_message(worker.uid,
                                               '🎉Ура! Ты внес более 5000 CZK🤑\n'
                                               '😱Теперь ты получаешь доступ в PRO-чат\n'
                                               'Для вступления отпиши сюда 👉🏻 @onegin_02')
                        await bot.send_message(main_config.ERROR_CHANNEL, 'LT\nНовый воркер в про чат: @{}\n'
                                                                     'Занес: {} CZK'.format(worker.username, total_sum))
                    else:
                        await bot.send_message(main_config.ERROR_CHANNEL, 'CZK \nВоркер: @{}\n'
                                                                     'Всего наворкал: {} CZK\n'
                                                                     'До про чата осталось: {} CZK'
                                               .format(worker.username, total_sum, (250000 - total_sum)))
                await MoneyNotifies.update.values(edited=True).where(MoneyNotifies.id == n.id).gino.status()
        except Exception as e:
            is_errors = True
            errors += f"Notify id: {n.id}: {e}\n"
    if is_errors:
        await bot.send_message(000, errors)
    await bot.close()


def get_rub(czk):
    return round(czk * 3.50, 0)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(check_notifies())
