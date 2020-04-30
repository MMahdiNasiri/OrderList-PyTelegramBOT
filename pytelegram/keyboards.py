from telebot import types
import telebot




def productkeyboard(*product):
    proditem = []
    markup = types.ReplyKeyboardMarkup(row_width=3)
    for x in product:
        proditem.append(types.KeyboardButton(x))
    finishitem = types.KeyboardButton('finish')

    markup.add(*proditem)
    markup.add(finishitem)
    return markup

def numberkeyboard():
    numbers = []
    markup = types.ReplyKeyboardMarkup(row_width=3)
    for x in range(1,13):
        numbers.append(types.KeyboardButton(str(x)))

    markup.add(*numbers)

    backItem = types.KeyboardButton('back')
    markup.add(backItem)
    return markup

