# import telebot


# bot = telebot.TeleBot(token='1064935072:AAEs8k05qJj3sGfhwfY_4fQfVYMn1ADXDnk')
myDict = {
    "1": "hello",
    "2": "whats up",
    "4": "how are you",
    "5": "bye"
}


file = open("newfile.txt", "r+")
text = f'{file.readline()} wow'
file.write(f'{str(myDict)}\n')

file.close()
print(text)