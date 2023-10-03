from aiogram import Router, types
from aiogram.filters import Command
from bot import scheduler, bot
from datetime import datetime
from db.shopdb import select_users

scheduler_router = Router()

@scheduler_router.message()
async def remind_me():
    for i in select_users():

        scheduler.add_job(
            send_reminder,
            "interval",
            seconds=4,
            args=i,
        )

async def send_reminder(user_id: int):
    await bot.send_message(str(user_id), "Это рассылка")

