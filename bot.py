import os
import telebot
from pybit.unified_trading import HTTP

BOT_TOKEN = os.getenv("BOT_TOKEN")
BYBIT_API_KEY = os.getenv("BYBIT_API_KEY")
BYBIT_API_SECRET = os.getenv("BYBIT_API_SECRET")

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
        result = bybit.get_wallet_balance(
            accountType="UNIFIED",
            coin="USDT"
        )

        if result.get("retCode") == 0:
            bot.reply_to(
                message,
                "✅ Bybit connection successful!"
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

bot.infinity_polling()
