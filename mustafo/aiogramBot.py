import logging
import asyncio
# from datetime import datatime

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import FSInputFile

TELEGRAM_TOKEN ="6476180980:AAHNbYz6_ALvd6FRkx3Ad3KGmsp24eotbiE"

# вывод отладочных сообщений в терминал
logging.basicConfig(level=logging.INFO)

# создали обьект bot
bot = Bot(token=TELEGRAM_TOKEN)

# создаем обьект диспетчер 
dp = Dispatcher()
# обрабатываем команду старт
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    
    image_from_pc = FSInputFile('stiker.webp')
    await message.answer_photo(image_from_pc, caption='Пообшаемся 🫦')
    await asyncio.sleep(2)
    await message.answer("Рад тебя видеть!")
@dp.message(Command('image'))
async def upload_photo(message: types.Message):
    image_from_pc = FSInputFile('stiker.webp')
    await message.answer_photo(image_from_pc, caption='Пообшаемся 🫦')

#ping pong
@dp.message()
async def echo(message: types.Message):
    await message.answer('бот от компании Google услышал: '+message.text)



# непрерывный режим работы бота в АССИНХРОННОМ режиме 
async def main():
    await dp.start_polling(bot)

# основной цикл
if __name__ == '__main__':
    asyncio.run(main())