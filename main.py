import os
import telebot
import dotenv
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

dotenv.load_dotenv()

TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	keyboard.add(
		KeyboardButton('Отправить заявку'),
		KeyboardButton('Посмотреть заявки')
	)
	bot.reply_to(message, 'Выберите действие', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()
