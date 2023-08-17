from telebot import types

class Keyboards:
    @staticmethod
    def get_main_keyboard():
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button1 = types.KeyboardButton("Кнопка 1")
        button2 = types.KeyboardButton("Кнопка 2")
        button3 = types.KeyboardButton("Инлайн-кнопки")
        button4 = types.KeyboardButton("Отправить медиа")
        keyboard.add(button1, button2, button3, button4)
        return keyboard
    
    @staticmethod
    def get_inline_keyboard():
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Инлайн кнопка 1", callback_data="button1")
        button2 = types.InlineKeyboardButton("Инлайн кнопка 2", callback_data="button2")
        keyboard.add(button1, button2)
        return keyboard
