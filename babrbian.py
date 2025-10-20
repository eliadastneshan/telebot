import telebot
bot=telebot.TeleBot('7999882647:AAFW0f1ooSkmSrKAxZCg2G4HGjGLRGqhjN8')
#@bot.message_handler(commands = ['start'])
#def welcome (message):
    #bot.send_message (message.chat.id,' خانه ای را که خداوند بنا نکند بنایانش زحمت بیهوده می کشند') 
@bot.message_handler(func=lambda message:True)
def echo_message( message):
    bot.reply_to(message ,'ما قهرمانهای ایرانیم')


bot.polling()
 