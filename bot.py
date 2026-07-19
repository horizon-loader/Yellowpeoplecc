import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=os.getenv('API_TOKEN'))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("hello, soon yellowpeople.cc in this bot")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
