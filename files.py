# import telebot


# bot = telebot.TeleBot(token='1064935072:AAEs8k05qJj3sGfhwfY_4fQfVYMn1ADXDnk')
myDict = {
    "1": "hello",
    "2": "whats up",
    "4": "how are you",
    "5": "bye"
}


file = open("newfile.txt", "a+")
text = f'{file.read()} wow'
file.write(str(myDict))
print(text)
file.close()