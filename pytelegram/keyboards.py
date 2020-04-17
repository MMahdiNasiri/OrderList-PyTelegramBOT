from telebot import types
import telebot




def productkeyboard(*product):
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
    numbers = []
    markup = types.ReplyKeyboardMarkup(row_width=3)
    for x in range(13):
        numbers.append(types.KeyboardButton(str(x)))

    markup.add(*numbers)

    backItem = types.KeyboardButton('back')
    markup.add(backItem)
    return markup

