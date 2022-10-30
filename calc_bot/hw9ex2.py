# Прикрутить бота к задачам с предыдущего семинара:
    # Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования

from telebot import TeleBot
import telebot
from telebot import types

bot = TeleBot('5621354309:AAGyrNvRtC22rYecWS44uNNsOu5UGG1amQY')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/рациональные")
    btn2 = types.KeyboardButton("/комплексные")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Здравствуй, {0.first_name}! Я калькулятор!"
                                           "Выбери действие".format(message.from_user), reply_markup=markup)


@bot.message_handler(commands=["рациональные"])
def handle_text(msg: telebot.types.Message):
        bot.send_message(msg.chat.id, text="Введите 2 числа и действие между ними")
        bot.register_next_step_handler(callback=viev_calc, message=msg)


def viev_calc(msg: telebot.types.Message):
        bot.send_message(chat_id=msg.from_user.id, text=calc(msg.text))


def calc(text):
    try:
        res = 0
        if "+" in text:
            lst = text.split('+')
            res = float(lst[0])+float(lst[1])
            return res
        elif "-" in text:
            lst = text.split('-')
            res = float(lst[0])-float(lst[1])
            return res
        elif "*" in text:
            lst = text.split('*')
            res = float(lst[0])*float(lst[1])
            return res
        elif "/" in text:
            lst = text.split('/')
            res = float(lst[0])/float(lst[1])
            return res
        else:
            res = 'Введите два числа разделенные знаком действия, например: 5+1'
            return res
    except:
        res = 'Непонятный мне знак'
        return res


@bot.message_handler(commands=["комплексные"])
def handle_text_comp(msg: telebot.types.Message):
    bot.send_message(msg.chat.id, text="Введите 2 комплексных числа"
                                           " например: 4+2j - 7-6j знак действия между комплексными числами отделяется пробелами")
    bot.register_next_step_handler(callback=viev_calc2, message=msg)


def viev_calc2(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,  text=compreh(msg.text))


def compreh(text):
    res = None
    lst = text.split()
    if lst[1] == '-':
        res = complex(lst[0]) - complex(lst[2])
        return str(res)
    elif lst[1] == '+':
        res = complex(lst[0]) + complex(lst[2])
        return str(res)
    elif lst[1] == '/':
        res = complex(lst[0]) / complex(lst[2])
        return str(res)
    elif lst[1] == '*':
        res = complex(lst[0]) * complex(lst[2])
        return str(res)
    else:
        print('Неверный ввод')
@bot.message_handler()
def error(msg: telebot.types.Message):
    bot.send_message(msg.from_user.id, "Я могу выполнять только одно действие, сделайте свой выбор заноо")


bot.polling(none_stop=True)