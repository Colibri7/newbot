import telebot

bot = telebot.TeleBot("2107161558:AAEMp0kLXpT6NNX6p5dtgqYtqlv5FQA-5p0")



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


# bot.infinity_polling()
bot.polling(none_stop=True)
