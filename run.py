import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router

TOKEN = "7623169097:AAGaKfmSqYbNJSQfhpfJ6JPcB530dL8ML8k"

# Logger sozlash
logging.basicConfig(level=logging.INFO)

# Bot, dispatcher va storage obyektlari
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Router obyektini yaratamiz
router = Router()
dp.include_router(router)

# Oddiy /start komandasi uchun handler
@router.message(lambda msg: msg.text == "/start")
async def start_handler(message: Message):
    await message.answer(f"Salom, {message.from_user.full_name}! Bot ishga tushdi ✅")

# Asosiy ishga tushirish funksiyasi
async def main():
    # Bot polling orqali ishlaydi
    await dp.start_polling(bot)

# Dastur ishga tushirish qismi
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot to'xtatildi ❌")

hqwj