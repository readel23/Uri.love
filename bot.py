import telebot

# Замените 'YOUR_TELEGRAM_BOT_TOKEN' на ваш токен бота
TOKEN = '6687885963:AAHNSaheHS7YlqaXiFPbLC-mPJLZCw-UCVc'

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Обработчик всех входящих сообщений


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


# Запускаем бота
bot.polling()
