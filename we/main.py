import telebot
import random 

API_TOKEN = "7228656911:AAHKx-WKOSo-FmTktzjrUhaF2TkVumxb2Os"

bot = telebot.TeleBot(API_TOKEN, parse_mode="HTML")


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "<b>Добро пожаловать!</b>")


@bot.message_handler(commands=["info"])
def send_info(message):
    help_text = (
        "<b>Доступные команды:</b>\n"
        "/start - запуск бота\n"
        "/info - список команд и функционал бота\n"
    )
    bot.reply_to(message, help_text)


@bot.message_handler(commands=['rad'])
def send_help(message):
    try:
        random_index = random.randint(0,5) 
        image_path = f"./img/image{random_index}.jpg"
        with open(image_path, 'rb') as image_file:
            bot.send_photo(message.chat.id, image_file)
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибк: {e}")



@bot.message_handler()
def handle_unknown_command(message):
    response = "<b>Простите я не знаю такой команды</b>."
    bot.reply_to(message, response)
    
    
    
       
bot.polling(none_stop=True)


