import os
import telebot

bot= telebot.TeleBot("1979069209:AAHaAghCZZEKGEp0QhEvUUUhTp305qrVJQE")

@bot.message_handler(commards-["start"])
def send_welcome(message):
    bot.reply_to(message,"Hello..! I'm WI TECH official bot")
    
@bot.message_handler(commands=["how"])
def.send_message(message):
    bot.send_message(message,"
http://youtube.com/channel/UCz0c1FI-mAXi2wqvDZA1PRQ")

bot.polling()