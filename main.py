import asyncio
import os
from aiogram import Bot, Dispatcher, types

from ui.keyboard import menu
from modules.username import username_scan
from modules.phone import phone_scan
from modules.email import email_scan
from modules.domain import domain_scan
from utils.ai import ai_analyze

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

user_state = {}

@dp.message()
async def handler(message: types.Message):
    text = message.text.strip()
    uid = message.from_user.id

    if text == "/start":
        await message.answer("osint panel ready", reply_markup=menu())
        return

    if text == "username scan":
        user_state[uid] = "username"
        await message.answer("send username")
        return

    if text == "phone scan":
        user_state[uid] = "phone"
        await message.answer("send phone number")
        return

    if text == "email scan":
        user_state[uid] = "email"
        await message.answer("send email")
        return

    if text == "domain scan":
        user_state[uid] = "domain"
        await message.answer("send domain")
        return

    if text == "ai analyze":
        user_state[uid] = "ai"
        await message.answer("send text for analysis")
        return

    mode = user_state.get(uid)

    if mode == "username":
        await message.answer(await username_scan(text))
        return

    if mode == "phone":
        await message.answer(phone_scan(text))
        return

    if mode == "email":
        await message.answer(email_scan(text))
        return

    if mode == "domain":
        await message.answer(domain_scan(text))
        return

    if mode == "ai":
        await message.answer(ai_analyze(text))
        return

    await message.answer("use /start")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
