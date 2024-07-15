from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '7217917723:AAFJE9lXSoHttOhw8FfhqUwKNQuwJQvaHNQ'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    chat_id = update.effective_chat.id
    link = "http://t.me/loot_box_box_bot/LOOTBOX"
    message = f"Hello! Tap here to visit the miniAPP: {link}"
    await context.bot.send_message(chat_id=chat_id, text=message)

def main() -> None:
    """Start the bot."""
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling()

if __name__ == '__main__':
    main()
