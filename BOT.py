import telebot
import requests
import random, sys, time, argparse, os, string
from datetime import datetime, timedelta
from telebot import types
from datetime import datetime
from array import *

TOKEN = "(Токен бота)"
bot = telebot.TeleBot(TOKEN)
group_id = ["@название_чата", "@название_чата"]
i = 0

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Рассылка")
    item2 = types.KeyboardButton("Таймер")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "я живой!".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    minuters = 0
    chat_id = message.chat.id
    text = message.text
    if message.chat.type == 'private':
        if text == 'Рассылка':
            bot.send_message(chat_id, 'Введите сообщение в формате: "Разослать: ваш_текст" без кавычек')
        elif text == 'Таймер':
            bot.send_message(chat_id, 'Введите сообщение в формате: "Время: кол-во_минут" без кавычек')
        elif 'Разослать: ' in text:
            msg = text.replace("Разослать: ","")
            if minuters == 0:
                bot.send_message(chat_id, 'Рассылка началась...')
                send_message_users(msg, text)
                bot.send_message(group_id, 'Рассылка завершена...')
            else:
                bot.send_message(chat_id, 'Рассылка началась...')
                send_message_users1(msg, text, minuters)
                bot.send_message(group_id, 'Рассылка завершена...')
       	elif 'Время: ' in text:
            minuters = text.replace("Время: ","")

def send_message_users(msg, text):
    for i in range(len(group_id)):
        bot.send_message(group_id[i], msg)
        i += 1

def send_message_users1(msg, text, minuters):
    sec = minuters * 60
    time.sleep(sec)
    bot.send_message(group_id, msg)

bot.polling(none_stop=True)
