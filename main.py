from core.middleware.middleware import DbSession
from aiogram import Bot, Dispatcher, F
from settings import settings
from core.handlers.basic import send_admin
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from core.handlers import appsheduler
from core.utilyti.queries_for_the_postgresql_database import Request
import contextlib
import asyncpg
import asyncio
import logging
from datetime import datetime


async def create_pool():
    return await asyncpg.create_pool(user='postgres', password='aarrttyyoomm', database='users', host='127.0.0.1',
                                     port=5432,
                                     command_timeout=60)


async def start_bot():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%('
                                                   'funcName)s(%(lineno)d) - %(message)s')

    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

    dp = Dispatcher()
    pool_connect = await create_pool()
    dp.update.middleware.register(DbSession(pool_connect))

    scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    scheduler.add_job(appsheduler.send_massage_to_week, trigger='cron', hour=datetime.now().hour,
                      minute=datetime.now().minute + 1, start_date=datetime.now(),
                      kwargs={'bot': bot})
    scheduler.add_job(appsheduler.send_message_to_day, trigger='cron', hour=datetime.now().hour,
                      minute=datetime.now().minute + 1, start_date=datetime.now(),
                      kwargs={'bot': bot})
    scheduler.start()

    dp.startup.register(send_admin)

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

    except Exception as ex:
        logging.error(f"[!!! Exception] - {ex}", exc_info=True)

    finally:
        await bot.session.close()


if __name__ == '__main__':
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(start_bot())
