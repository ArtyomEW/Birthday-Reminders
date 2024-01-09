from aiogram import Bot
from settings import settings


async def send_admin(bot: Bot):
    await bot.send_message(settings.bots.admin_id, 'Бот запущен')

