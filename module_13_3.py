from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor

API_TOKEN = ''

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.")


@dp.message_handler()
async def all_messages(message: Message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == '__main__':
    print("Bot is running...")
    executor.start_polling(dp, skip_updates=True)
