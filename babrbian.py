from telebot import TeleBot
from config import API_TOKEN

bot = TeleBot (API_TOKEN)
@bot.message_handler(commands = ['start'])
def welcome (message):
    bot.send_message (message.chat.id,' خانه ای را که خداوند بنا نکند بنایانش زحمت بیهوده می کشند') 



bot.polling()
 