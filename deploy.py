import telebot
from telebot import types
import os

TOKEN = os.environ.get('1605385540:AAGvNZOSXrd9Rp819gm85eHA9_bSrbk6pUY')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_more = types.InlineKeyboardButton(text='Узнать больше', callback_data='more')
    item_wa = types.InlineKeyboardButton(text='Зарегистрироваться через WA',
                                         url='https://wa.me/+996556280688')
    markup_inline.add(item_more, item_wa)
    bot.send_message(message.chat.id, 'Как тебя зовут?',
                     reply_markup=markup_inline
                     )


@bot.callback_query_handler(func=lambda call: True)
def hello(call):
    if call.data == 'more':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_info = types.KeyboardButton('Информация')
        item_price = types.KeyboardButton('Цена')
        markup_reply.add(item_info, item_price)
    bot.send_message(call.message.chat.id, 'Что вас интересует?',
                     reply_markup=markup_reply
                     )


@bot.message_handler(content_types=['text'])
def t(message):
    if message.text == 'Информация':
        print('a')
    elif message.text == 'Цена':
        pass



bot.polling()
