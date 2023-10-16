# имя бота coddyMustafo
# никнейм бота coddyMustafoBot
# ссылка на бота https://t.me/coddyMustafoBot

# token = "6370332659:AAFlPYUroe7kLM41miLbCQ0nzahLKvFc1O4"
import telebot

# импортируем из библиотеки time метод sleep
from time import sleep
from telebot import types
import random
import webbrowser

TOKEN = "6370332659:AAFlPYUroe7kLM41miLbCQ0nzahLKvFc1O4"

# библиотека телебот содержить класс  TeleBot

# обект     = библиотека.класс(свойства)
mySuperBot = telebot.TeleBot(TOKEN)


# обработчик команды /start
@mySuperBot.message_handler(commands=["start"])
def obrabotkaKomandiStart(message):
    # создаем клавиатуру с 2 кнопками
    raskladka1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    levoeknopka = types.KeyboardButton("Кто ты")
    pravayaknopka = types.KeyboardButton("Кубик брость?")
    raskladka1.add(levoeknopka, pravayaknopka)

    # mySuperBot.send_message(комуОтправить, какое собщениеОтправить)
    mySuperBot.send_message(
        message.chat.id,
        "Ассаламу алейкум ва рахматулохи баракату, {0.first_name}. \n Это <b>{1.first_name}</b>. Меня создал Мустафо".format(
            message.from_user, mySuperBot.get_me()
        ),
        parse_mode="html",
        reply_markup=raskladka1,
    )

@mySuperBot.message_handler(commands=['site'])
def site(messge):
    sleep(1)
    mySuperBot.send_chat_action(messge.chat.id, "typing")
    mySuperBot.send_message(messge.chat.id, 'В этой школе я обучался')
    sleep(2)
    webbrowser.open("https://coddyschool.com/")

@mySuperBot.message_handler(content_types=["text"])
def lalala(message):
    if message.chat.type == "private":
        if message.text == "Кто ты":
            raskladkavibora = types.InlineKeyboardMarkup(row_width=2)
            leftButton = types.InlineKeyboardButton("не знаю", callback_data="good")
            RightButton = types.InlineKeyboardButton("ты пророжденный гений", callback_data="bad")
            raskladkavibora.add(leftButton,RightButton)
            mySuperBot.send_message(message.chat.id, "а ты как думаеш", reply_markup=raskladkavibora)
        elif message.text == "Кубик брость?":
            mySuperBot.send_message(message.chat.id, str(random.randint(1, 6)))

        else:
            otvet1 = "даже не знаю что сказать :("
            otvet2 = "Даыай потом поговорим я щас домашку делаю ;)"
            otvet3 = "Хей!!!! Нормально пиши ладно а то........."
            otvet4 = "НУ я немогу ответит брат!!;)"
            otvet5 = "не хочу ответит на этот вопрос.....у меня нет подхадаших команд на этот вопрос"
            sleep(1)
            mySuperBot.send_chat_action(message.chat.id, "typing")
            nechevoskazat = [otvet1, otvet2, otvet3, otvet4, otvet5]
            mySuperBot.send_message(message.chat.id, random.choice(nechevoskazat))

            # отпрака такого же текаста
            # mySuperBot.send_message(message.chat.id, message.text)


@mySuperBot.message_handler(commands=["bye"])
def obrabotkaKomandiStart(message):
    mySuperBot.send_chat_action(message.chat.id, "typing")

    # mySuperBot.send_message(комуОтправить, какое собщениеОтправить)
    mySuperBot.send_message(message.chat.id, "пока")

@mySuperBot.callback_query_handler(func=lambda call: True)
def otvetNaknopki(call):
    try:
        if call.message:
            if call.data == 'good':
                mySuperBot.send_message(call.message.chat.id, 'Я искуственный интелект пришел захватит мир')
            elif call.data == 'bad':
                mySuperBot.send_message(call.message.chat.id, 'и как ты узнал'.format(call.from_user))
            sleep(2)
            mySuperBot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Кто ты',reply_markup=None)
    except Exception as e:
        print(repr(e))

# запуск бота
mySuperBot.polling(none_stop=True)