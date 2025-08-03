from telegram import Update
from telegram.ext import ContextTypes
from wolfram_client import query_wolfram
from .main import BOT_USERNAME

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello im the Wolfram Bot! How can i help you?")


async def handle_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query_type = update.message.chat.type
    query = update.message.text

    print(f'User ({update.message.chat.id}) in {query_type}: "{query}"')

    if query_type in ["group", "supergroup"]:
        if BOT_USERNAME in query:
            new_query = query.replace(BOT_USERNAME, "").strip()
            result = query_wolfram(new_query)
        else:
            return  
    else:
        result = query_wolfram(query)

    print('Bot:', result)
    await update.message.reply_text(result) #    await update.message.reply_text(query_wolfram(update.message.reply_text))


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Updates {update} caused error {context.error}")
