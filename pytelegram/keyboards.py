

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
    for x in range(1,13,3):
        markup.row(numbers[x], numbers[x+1], numbers[x+2])
    markup.row(backItem)
    return markup