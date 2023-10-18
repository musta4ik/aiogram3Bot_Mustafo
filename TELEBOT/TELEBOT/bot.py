# имя бота coddyMustafo
# никнейм бота coddyMustafoBot
# ссылка на бота https://t.me/coddyMustafoBot

# token = "6370332659:AAFlPYUroe7kLM41miLbCQ0nzahLKvFc1O4"
import telebot
#импортируем из библиотеки time метод sleep
from time import sleep
from telebot import types
import random
TOKEN = "6370332659:AAFlPYUroe7kLM41miLbCQ0nzahLKvFc1O4"

#библиотека телебот содержить класс  TeleBot

#обект     = библиотека.класс(свойства)
mySuperBot = telebot.TeleBot(TOKEN)

#обработчик команды /start
@mySuperBot.message_handler(commands=['start'])
def obrabotkaKomandiStart(message):
    
    #создаем клавиатуру с 2 кнопками
    raskladka1=types.ReplyKeyboardMarkup(resize_keyboard=True)
    levoeknopka =types.KeyboardButton('Как дела')
    pravayaknopka =types.KeyboardButton('Кубик брость?')
    raskladka1.add(levoeknopka, pravayaknopka)
   
    # mySuperBot.send_message(комуОтправить, какое собщениеОтправить)
    mySuperBot.send_message(message.chat.id, "Ассаламу алейкум ва рахматулохи баракату, {0.first_name}. \n Это <b>{1.first_name}</b>. Меня создал Мустафо".format(message.from_user, mySuperBot.get_me()), parse_mode='html', reply_markup=raskladka1)
@mySuperBot.message_handler(content_types=["text"])
def lalala(message):
    if message.chat.type=='private':
        if message.text=='Как дела':
            mySuperBot.send_message(message.chat.id, 'все норм серегей сергеевич ')
        elif message.text == 'Кубик брость?':
            mySuperBot.send_message(message.chat.id, 'нет пока что ')
        else:
            otvet1 = "даже не знаю что сказать :("
            otvet2 = "Даыай потом поговорим я щас домашку делаю ;)"
            nechevoskazat = [otvet1,otvet2]
            mySuperBot.send_message(message.chat.id, random.choice(nechevoskazat))
            
            #отпрака такого же текаста 
            #mySuperBot.send_message(message.chat.id, message.text)
            
            
@mySuperBot.message_handler(commands=['bye'])

def obrabotkaKomandiStart(message):
    mySuperBot.send_chat_action(message.chat.id, "typing")

    # mySuperBot.send_message(комуОтправить, какое собщениеОтправить)
    mySuperBot.send_message(message.chat.id, "пока")
#запуск бота
mySuperBot.polling(none_stop = True)
