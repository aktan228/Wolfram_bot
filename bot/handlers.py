from telegram import Update
from telegram.ext import ContextTypes
from wolfram_client import query_wolfram
from .main import BOT_USERNAME
from PIL import Image
import pytesseract
import os
from io import BytesIO
from latex_renderer import LatexRenderer

renderer = LatexRenderer()

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello im the Wolfram Bot! How can i help you?")


async def handle_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query_type = update.message.chat.type
    query = update.message.text
    message= update.message
    
    if update.message.text:
        query = update.message.text
    elif update.message.photo:
        photo_file = await update.message.photo[-1].get_file()
        photo_bytes = await photo_file.download_as_bytearray()
        
        #OCR
        img = Image.open(BytesIO(photo_bytes))
        query = pytesseract.image_to_string(img)
        
        if not query.strip():
            await update.message.reply_text('Couldnt recognize text on photo')
            return
    else:
        await update.message.reply_text("Send text or photo with formula")
        return

    print(f'User ({update.message.chat.id}) in {query_type}: "{query}"')

    if query_type in ["group", "supergroup"]:
        if BOT_USERNAME in query:
            new_query = query.replace(BOT_USERNAME, "").strip()
            result = query_wolfram(new_query)
        else:
            return  
    else:
        result = query_wolfram(query)

    if 'latex' in result:
        filename = renderer.render(result['latex'])
        with open(filename, 'rb') as img_file:
            await message.reply_photo(img_file)
        os.remove(filename)
    elif "plaintext" in result:
        await message.reply_text(result["plaintext"])
        
    else:
        await message.reply_text(result.get("error","No result found"))
    print('Bot:', result)
    await update.message.reply_text(result) #    await update.message.reply_text(query_wolfram(update.message.reply_text))


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Updates {update} caused error {context.error}")
