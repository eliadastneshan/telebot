from telebot import TeleBot
from config import API_TOKEN

bot = TeleBot (API_TOKEN)

user_ID = []
@bot.message_handler(commands = ['start'])
def welcome (message):
    bot.send_message (message.chat.id,' خانه ای را که خداوند بنا نکند بنایانش زحمت بیهوده می کشند') 
    if message.chat.id not in user_ID:
        user_ID.append(message.chat.id)

@bot.message_handler(commands=['دیدن لیست'])
def send_update(message):
    for id in user_ID:
        bot.send_message (id,'لیست اجناس')



bot.polling()
 
