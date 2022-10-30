from ast import Return
from telebot import TeleBot
from telebot import types

bot = TeleBot('5621354309:AAGyrNvRtC22rYecWS44uNNsOu5UGG1amQY')

@bot.message_handler(commands=['start'])
def but_ts(message):
    murkup = types.InlineKeyboardMarkup(row_width=3) # создали онлайн клавиатуру
    button_1 = types.InlineKeyboardButton(text='Список телефонов', callback_data='id_1' ) # создали кнопку
    button_2 = types.InlineKeyboardButton(text='Поиск контака', callback_data='id_2' ) # создали кнопку
    button_3 = types.InlineKeyboardButton(text='Скачать справочник', callback_data='id_3' ) # создали кнопку
    button_4 = types.InlineKeyboardButton(text='Добавить контакт', callback_data='id_4' ) # создали кнопку
    button_5 = types.InlineKeyboardButton(text='Импорт контактов', callback_data='id_5' ) # создали кнопку
    murkup.add(button_1,button_2,button_3,button_4,button_5) # добавили кнопку в клавиатуру
    bot.send_message(message.chat.id, 'Добро пожаловать в телефоный справочник', reply_markup = murkup) 



with open('phone_book.txt', 'r', encoding='utf-8') as st:
    data = st.read()

@bot.callback_query_handler(func= lambda call: True)
def callback_1(call):    
    if call.message:
        if call.data == 'id_1':
            with open('phone_book.txt', 'r', encoding='utf-8') as st:
                data = st.read()
                bot.send_message(call.message.chat.id, data)
        elif call.data == 'id_2':
            bot.send_message(call.message.chat.id, 'Кто Вам нужен?')
            @bot.message_handler(content_types = 'text')
            def search_data(message):
                search_value = message.text
                with open('phone_book.txt','r', encoding='utf-8') as file:
                    count = 0
                    for line in file:
                        if search_value in line:
                            bot.send_message(message.chat.id, f'Вы искали {line}')
                            count = count + 1
                    if count == 0:
                        bot.send_message(call.message.chat.id, f'Контакта с такими данными тут нет')                                                                                                      
        elif call.data == 'id_3':
            doc = open('phone_book.txt', 'rb')
            bot.send_document(call.message.chat.id, document=doc)
        elif call.data == 'id_4':
            bot.send_message(call.message.chat.id, f'Добавьте ФИО и номер телефона')
            @bot.message_handler(content_types='text')
            def add_contact(message):
                doc = open('phone_book.txt', 'a', encoding='utf-8')
                doc.write("\n{imia}".format(imia=message.text))                                                           
        elif call.data == 'id_5':
            bot.send_message(call.message.chat.id, f'Добавьте файл с данными, которые хотите добавить')
            @bot.message_handler(content_types='document')
            def add_information(message: types.Message):
                file = bot.get_file(message.document.file_id)
                downloaded_file = bot.download_file(file.file_path)
                message.document.file_name = 'temp.txt'
                with open('temp.txt', 'wb') as f_out:
                    f_out.write(downloaded_file)
                with open('temp.txt', "r", encoding='utf-8') as f, open('phone_book.txt', "a", encoding='utf-8') as g:
                    g.writelines('\n')
                    for line in f:
                        if len(line) > 20:
                            g.writelines(line)                            
                    if len(line) < 20:
                        with open('temp.txt', encoding='utf-8') as k:
                            lines = k.readlines()
                        with open('phone_book.txt', "a", encoding='utf-8') as l:
                            j = 0
                            lst1 = []
                            for each in lines:
                                if not each.__contains__(','):
                                    if each != '\n':
                                        lst1.append(each.replace("\n", ""))
                                        j += 1
                                        if j == 3:
                                            l.writelines(', '.join(lst1))
                                            l.writelines('\n')
                                            j = 0
                                            lst1 = []                    
                                            

bot.polling(non_stop=True)

