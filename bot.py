import telebot
from telebot import types
token = "6814985471:AAFZrC8ASlB4NiGv6pDp6XVHL9pbJA3lUto"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton("Година")
    item2 = types.KeyboardButton("Допомога")
    item3 = types.KeyboardButton("Інше")

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, 'Привіт, {0.first_name}!'.format(message.from_user), reply_markup = markup )

@bot.message_handler(commands=['text'])
def asd(message):
    if message.chat.type == 'private':
        if message.text == 'Година':
            bot.send_message(message.chat.id, 'Ти маэш позвонити мамы о 22:00!')
    elif message.text == "Допомога":
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton("АА")
        item2 = types.KeyboardButton("Айц")
        back = types.KeyboardButton("Назад")
        markup.add(item1, item2, back)

        bot.send_message(message.chat.id, 'Допомога', reply_markup=markup)

    elif message.text == "Інше":
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton("АА")
        item2 = types.KeyboardButton("Айц")
        back = types.KeyboardButton("Назад")
        markup.add(item1, item2, back)

    bot.send_message(message.chat.id, 'Інше', reply_markup = markup )

bot.polling(none_stop=True)