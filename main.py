import random
import conf
import telebot
import pars
from telebot import types

bot=telebot.TeleBot('2047998633:AAHzCvalrxEeHJtHK8DCtoufFS_U4dIysx0')



key1=telebot.types.ReplyKeyboardMarkup(True,True)
key1.add('поиск','Анекдоты',"/geophone",'Меню','Погода','Пока','Футбол','Курс','Вакансии')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет ты написал мне /start,',reply_markup=key1)


@bot.message_handler(commands=["geophone"])
def tel(message):
    keyboard = types.ReplyKeyboardMarkup(True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_phone, button_geo,"/start")
    bot.send_message(message.chat.id, "Отправь мне свой номер телефона или поделись местоположением, жалкий человечишка!",reply_markup=keyboard)

@bot.message_handler(content_types=["text"])

def reap(message):
    if message.text.lower() == 'погода':
        keyboard = types.InlineKeyboardMarkup()
        b12 = types.InlineKeyboardButton(text='Погода в Нижнем Тагиле', callback_data="a1")
        keyboard.add(b12)
        bot.send_message(message.from_user.id, text='Нажми на кнопку', reply_markup=keyboard)
    if message.text.lower() == 'курс':
        bot.send_message(message.chat.id,pars.pars2())
    elif message.text.lower()=='футбол':
        keyboard = types.InlineKeyboardMarkup()
        b12 = types.InlineKeyboardButton(text='Турнирная таблица Апл', callback_data="a2")
        b13 = types.InlineKeyboardButton(text='Турнирная таблица Рпл', callback_data="a3")
        keyboard.add(b12)
        keyboard.add(b13)
        bot.send_message(message.from_user.id, text='Нажми на кнопку', reply_markup=keyboard)


    elif message.text.lower()=='вакансии':
        keyboard = types.InlineKeyboardMarkup()
        b1=types.InlineKeyboardButton(text='Вакансии Python',callback_data='python')
        keyboard.add(b1)
        bot.send_message(message.from_user.id, text='Нажми на кнопку', reply_markup=keyboard)

    elif message.text.lower() == 'привет':
        bot.send_message(message.chat.id,'привет мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower()=='я тебя люблю':
        bot.send_sticker(message.chat.id,'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
    elif message.text.lower()=='поиск':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)
    elif message.text=="Анекдоты":
        keyboard=types.InlineKeyboardMarkup()
        b1=types.InlineKeyboardButton(text='Анекдоты',callback_data="b1")
        keyboard.add(b1)
        bot.send_message(message.from_user.id,text='Нажми на кнопку',reply_markup=keyboard)
    elif message.text=='Меню':
        k=types.InlineKeyboardMarkup()
        bab1=types.InlineKeyboardButton(text='Суп ',callback_data='bab1')
        b2=types.InlineKeyboardButton(text='Салат',callback_data='b2')
        b3=types.InlineKeyboardButton(text='Пюре',callback_data='b3')
        menu=types.InlineKeyboardButton(text='Корзина',callback_data='menu')
        k.add(bab1,b2,b3,menu)
        bot.send_message(message.from_user.id,text='Выбери блюдо',reply_markup=k)
    elif message.text=="Картинка":
        p=open('img.png','rb')
        bot.send_photo(message.chat.id,p)

    else:
        bot.send_message(message.chat.id,'Выбери кнопку и я тебе отвечу))')



@bot.callback_query_handler(func=lambda call: True)
def boter(call):
    if call.data=='b1':
        f=conf.anek
        bot.send_message(call.message.chat.id,f)
    elif call.data=="bab1":
        p = open('img.png', 'rb')
        bot.send_photo(call.message.chat.id, p)
        bot.send_message(call.message.chat.id,'Стоимость 1 рубль')
        k=types.InlineKeyboardMarkup()
        syp1=types.InlineKeyboardButton(text='Добавить в корзину',callback_data='syp1')
        k.add(syp1)
        bot.send_message(call.message.chat.id,text='Если хотите добавить в корзину жмите!', reply_markup=k)

    elif call.data=='syp1':
        bot.send_message(call.message.chat.id,'Добавлено')
        bot.send_message(call.message.chat.id, 'Чтобы вернуться в меню напишие "Меню" ')
        s='Суп'
    elif call.data == 'syp2':
        bot.send_message(call.message.chat.id, 'Добавлено')
        bot.send_message(call.message.chat.id, 'Чтобы вернуться в меню напишие "Меню" ')
        pik='Салат'
    elif call.data == 'syp3':
        bot.send_message(call.message.chat.id, 'Добавлено')
        bot.send_message(call.message.chat.id, 'Чтобы вернуться в меню напишие "Меню" ')
        g='Пюре'

    elif call.data=="b2":
        p = open('img_1.png', 'rb')
        bot.send_photo(call.message.chat.id, p)
        bot.send_message(call.message.chat.id, 'Стоимость 1 рубль')
        k = types.InlineKeyboardMarkup()
        syp2 = types.InlineKeyboardButton(text='Добавить в корзину', callback_data='syp2')
        k.add(syp2)
        bot.send_message(call.message.chat.id, text='Если хотите добавить в корзину жмите!', reply_markup=k)
    elif call.data=='b3':
        p = open('img_2.png', 'rb')
        bot.send_photo(call.message.chat.id, p)
        bot.send_message(call.message.chat.id, 'Стоимость 1 рубль')
        k = types.InlineKeyboardMarkup()
        syp3 = types.InlineKeyboardButton(text='Добавить в корзину', callback_data='syp3')
        k.add(syp3)
        bot.send_message(call.message.chat.id, text='Если хотите добавить в корзину жмите!', reply_markup=k)
    elif call.data=='menu':

        k=types.InlineKeyboardMarkup()
        a=types.InlineKeyboardButton(text='1',callback_data='a')
        k.add(a)
        bot.send_message(call.message.chat.id,text='Это корзина'  ,reply_markup=k)
    elif call.data=="a1":
        a1=pars.s
        a2=pars.s1
        bot.send_message(call.message.chat.id, a2)
        bot.send_message(call.message.chat.id, a1)

    elif call.data=='python':
        python=pars.pars3()
        for i in range(len(python)):
            bot.send_message(call.message.chat.id,python[i])
    elif call.data=="a2":
       b=pars.pars()
       for i in range(len(b)):
        bot.send_message(call.message.chat.id,b[i])
    elif call.data=="a3":
       b=pars.pars1()
       for i in range(len(b)):
        bot.send_message(call.message.chat.id,b[i])






    bot.polling()