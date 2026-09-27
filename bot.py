import os
import telebot
import urllib.request
from pybit.unified_trading import HTTP

BOT_TOKEN = os.getenv("BOT_TOKEN")
BYBIT_API_KEY = os.getenv("BYBIT_API_KEY")
BYBIT_API_SECRET = os.getenv("BYBIT_API_SECRET")

@bot.message_handler(commands=["checkkey"])
def check_key(message):
    key = os.getenv("BYBIT_API_KEY", "")
    secret = os.getenv("BYBIT_API_SECRET", "")

    bot.reply_to(
        message,
        f"🔑 API key ending: {key[-4:] if key else 'MISSING'}\n"
        f"🔐 API secret present: {'YES' if secret else 'NO'}"
    )
bot = telebot.TeleBot(BOT_TOKEN)

bybit = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET
)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "🤖 Bybit P2P Assistant is online!\n\n"
        "Use /bybit to test the Bybit connection."
    )
@bot.message_handler(commands=["bybit"])
def bybit_test(message):
    try:
        result = bybit.get_open_orders(
            category="spot",
            openOnly=0
        )

        if result.get("retCode") == 0:
            bot.reply_to(
                message,
                "✅ Bybit API connection successful!"
            )
        else:
            bot.reply_to(
                message,
                f"❌ Bybit returned an error:\n{result.get('retMsg')}"
            )

    except Exception as e:
        bot.reply_to(
            message,
            f"❌ Connection error:\n{str(e)}"
        )
@bot.message_handler(commands=["ip"])
def get_ip(message):
    try:
        ip = urllib.request.urlopen("https://api.ipify.org", timeout=10).read().decode()
        bot.reply_to(message, f"🌐 Railway public IP:\n{ip}")
    except Exception as e:
        bot.reply_to(message, f"❌ Could not get IP:\n{str(e)}")

bot.infinity_polling()
