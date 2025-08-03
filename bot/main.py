import os
from typing import Final
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
from telegram import Update
from dotenv import load_dotenv

BOT_USERNAME: Final = "@WolframHelperrrBot"

load_dotenv()


def main():
    print("Starting bot")
    app = Application.builder().token(os.getenv("TELEGRAM_TOKEN")).build()

    #Commands
    app.add_handler(CommandHandler("start", start_command))
    
    #Messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_query))

    #Errors
    app.add_error_handler(error)
    
    #Polling
    print('Polling...')
    app.run_polling()
    
if __name__ == '__main__':
    main()