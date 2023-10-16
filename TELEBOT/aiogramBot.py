import logging
import asyncio   
# from datetime import datatime

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject
from aiogram.types import FSInputFile
from random import randint
TELEGRAM_TOKEN ="6476180980:AAHNbYz6_ALvd6FRkx3Ad3KGmsp24eotbiE"
Group_ID = "-1001674247269"
# вывод отладочных сообщений в терминал
logging.basicConfig(level=logging.INFO)

# создали обьект bot
bot = Bot(token=TELEGRAM_TOKEN)

# создаем обьект диспетчер 
dp = Dispatcher()
# обрабатываем команду старт
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    
    image_from_pc = FSInputFile('stiker.png')
    await message.answer_photo(image_from_pc, caption='Пообшаемся 🫦')
    await asyncio.sleep(2)
    await message.answer("Рад тебя видеть!, <b>{0.username}</b>! ".format(message.from_user), parse_mode='html')
#обработчик команды рандом
# /rnd 1-30
@dp.message(Command(commands=['random', 'rand', 'rnd']))
async def get_random(message: types.Message, command: CommandObject):
    rnum = randint(1,6)
    await message.reply(f'Случайное число получилось:  \t {rnum}')
@dp.message(Command('image'))
async def upload_photo(message: types.Message):
    image_from_pc = FSInputFile('stiker.png')
    await message.answer_photo(image_from_pc, caption='Пообшаемся 🫦')

@dp.message(Command('mygroup'))
async def cmd_to_group(message: types.Message, bot: Bot):
    await bot.send_message(Group_ID, "Hello from Mustafo")

#ping pong
@dp.message()
async def echo(message: types.Message):
    print('message listened')
    # await message.answer('бот Mustafo услышал: '+message.text)







# непрерывный режим работы бота в АССИНХРОННОМ режиме 
async def main():
    await dp.start_polling(bot)

# основной цикл
if __name__ == '__main__':
    asyncio.run(main())