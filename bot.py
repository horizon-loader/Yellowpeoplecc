import os
import telebot

bot = telebot.TeleBot(os.getenv('API_TOKEN'))

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "hello, soon yellowpeople.cc in this bot")

bot.polling()
