import telebot
import time
import sys
from telebot import types


bot = telebot.TeleBot(token = "1064935072:AAEs8k05qJj3sGfhwfY_4fQfVYMn1ADXDnk")

product = ['apple', 'orange', 'cucumber', 'banana', 'strawberry', 'melon']
id_order = dict()
order = dict()

class orders:
    def __init__(self):
        self.tags = {}
    def __setitem__(self, tag, value):
        self.tags[tag] = value
    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)




def productkeyboard():
    proditem = {}
    markup = types.ReplyKeyboardMarkup()
    for x in range(len(product)):
        proditem[x] = types.KeyboardButton(product[x])
    finishitem = types.KeyboardButton('finish')
    for x in range(0,len(product),3):
        markup.row(proditem[x], proditem[x+1], proditem[x+2])
    markup.row(finishitem)
    return markup

def numberkeyboard():
    numbers = {}
    markup = types.ReplyKeyboardMarkup()
    for x in range(13):
        numbers[x] = types.KeyboardButton(str(x))
    backItem = types.KeyboardButton('back')
    for x in range(1,12,3):
        markup.row(numbers[x], numbers[x+1], numbers[x+2])
    markup.row(backItem)
    return markup



@bot.message_handler(commands=['start', 'help'])
def starting_message(message):
    markup = productkeyboard()
    bot.send_message(message.chat.id, 'choose product from the list', reply_markup=markup)




@bot.message_handler(func=lambda x: x.text.lower() in product)
def get_order(message):
    id_order[message.chat.id] = message.text.lower()
    markup = numberkeyboard()
    bot.send_message(message.chat.id, "how much do you want", reply_markup=markup)




@bot.message_handler(regexp='[0-9]')
def number_order(message):
    chat_id = message.chat.id
    if chat_id in id_order:
        reserve = id_order[chat_id]
        if chat_id not in order:
            order[chat_id] = orders()
        order[chat_id].tags[reserve] = message.text
        msg = f'your orders until now:\n{order[chat_id].tags}'
        markup = productkeyboard()
        bot.send_message(chat_id, msg, reply_markup=markup)





@bot.message_handler(func=lambda message: (message.text == 'finish') or (message.text.lower()=='back'))
def save_order(message):
    chat_id = message.chat.id
    markup = productkeyboard()
    if message.text == 'back':
        bot.send_message(chat_id , "what???", reply_markup=markup)
    if message.text == 'finish':    
        if chat_id in order:
            msg = ""
            for product,value in order[chat_id].tags.items():
                msg += f"{product} : {value}\n"
            del order[chat_id]
            bot.send_message(chat_id , f"your order is:\n{msg}you can /start again", reply_markup=markup)






@bot.message_handler(func=lambda x: x.text != "back" and x.text != "finish")
def wrong_message(message):
    chat_id = message.chat.id
    if chat_id in id_order:
        markup = numberkeyboard()
        bot.send_message(chat_id, 'you must enter a number!!!!', reply_markup=markup)
    else:
        markup = productkeyboard()
        bot.send_message(chat_id, "you must choose what you want first!!!", reply_markup=markup)
    



while True:
    bot.polling()
