import os
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "🤖 Bybit P2P Assistant is online!\n\n"
        "Use /status to check the bot."
    )

@bot.message_handler(commands=["status"])
def status(message):
    bot.reply_to(message, "✅ Bot is online and responding.")

bot.infinity_polling()
