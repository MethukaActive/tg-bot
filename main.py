import os
import telebot


bot = telebot.TeleBot("http://t.me/methukaactivebot")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm methu pro Chat Bot")


@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message.chat.id, "https://www.youtube.com/channel/UC9IWiBeii67v_LZZXEQhM7w")



bot.polling()
