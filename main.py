#импорт нужных библеотек
import os
import telebot
from telebot import types
from keyboards import Keyboards

TOKEN = "6216361737:AAH7qkFEIgZf6MLEEoIFjyoepTFjW2tyV7I" #указываем токен который получили от BotFather
bot = telebot.TeleBot(TOKEN) #Создаем переменную bot которую будем использовать позже после указываем в ней токен бота

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Выберите действие:", reply_markup=Keyboards.get_main_keyboard()) #Сдесь мы создаем команду start и указываем что она должна делать команда указывается в [] скобках и с обязательным методом command=

@bot.message_handler(func=lambda message: message.text == "Кнопка 1")
def handle_button1(message):
    bot.send_message(message.chat.id, "Вы нажали кнопку 1") #Здесь мы указываем обычную кнопку методом messange_handler используя лямбда функцию а так же указываем взаимодействие с пользователем через bot.send_message и используя chat_id пишем сообщение

@bot.message_handler(func=lambda message: message.text == "Кнопка 2")
def handle_button2(message):
    bot.send_message(message.chat.id, "Вы нажали кнопку 2")

@bot.message_handler(func=lambda message: message.text == "Отправить медиа")
def handle_media(message):
    bot.send_message(message.chat.id, "Вот ваше медиа:")
    bot.send_photo(message.chat.id, open('C:/Users/nurbe/OneDrive/Документы/keysbot/image/flask.png', 'rb'))  # Путь к изображению
    bot.send_animation(message.chat.id, open('C:/Users/nurbe/OneDrive/Документы/keysbot/image/XOsX.gif', 'rb'))  # Путь к анимации (гифке)
    bot.send_video(message.chat.id, open('C:/Users/nurbe/OneDrive/Документы/keysbot/image/C vs C++ vs C#.mp4', 'rb'))  # Путь к видео
    bot.send_message(message.chat.id, "А также ссылка: https://kwork.ru/projects?a=1&keyword=Python")

#выше так же используя @bot.messange_handler и создавая функцию def hendle_media и указывая внутри параметр (message), мы вызываем от бота отправку, фото,гиф,видео, и ссылки, В Python, rb означает "read binary" (чтение в двоичном режиме). Это режим открытия файла для чтения в двоичном формате, который используется, например, при работе с изображениями, анимацией (гифками), видео и другими бинарными файлами.
#таким же образом можно создать для каждого файла отдельную кнопку

@bot.message_handler(func=lambda message: message.text == "Инлайн-кнопки")
def handle_inline_buttons(message):
    bot.send_message(message.chat.id, "Выберите инлайн-кнопку:", reply_markup=Keyboards.get_inline_keyboard())

@bot.callback_query_handler(func=lambda call: call.data == "button1")
def handle_inline_button1(call):
    bot.send_message(call.message.chat.id, "Вы выбрали инлайн кнопку 1")

@bot.callback_query_handler(func=lambda call: call.data == "button2")
def handle_inline_button2(call):
    bot.send_message(call.message.chat.id, "Вы выбрали инлайн кнопку 2")

#выше мы обращаемся к инлайн кнопкам в нашем keyboards.py с помощью reply_markup=Keyboards.get_inline_keyboard()), reply_markup= это метод который перебрасывает вас к определенному методу(кнопкам),
#и после вызова инлайн кнопок, мы начинаем взаимодействие с ними callback_query_handler это метод для работы с инлайн кнопками


if __name__ == "__main__":
    bot.polling(none_stop=True) #запускаем бота
