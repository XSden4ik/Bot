import telebot

token = "6814985471:AAFZrC8ASlB4NiGv6pDp6XVHL9pbJA3lUto"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcom(mesenge):
    bot.send_message(mesenge.chat.id, 'Привіт,я бот який створений Денисом для Юри.Користуйся такими командами як /hors та /thanks .Звертйся:D')

@bot.message_handler(commands=['hors'])
def hors(mesenge):
    bot.send_message(mesenge.chat.id, 'Нагадую,ти маєш позвонити мамі о 22:00!')


@bot.message_handler(commands=['thanks'])
def thanks(mesenge):
    bot.send_message(mesenge.chat.id, 'Немає за що,звертайся якщо буду потрібним :D')


bot.polling(none_stop=True)