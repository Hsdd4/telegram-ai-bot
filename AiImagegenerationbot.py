# Pollinations AI Image Generator via Telegram in Python

import os
import requests
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Fetch token from environment variable or paste directly
BOT_TOKEN = os.getenv("BOT_TOKEN") or "YOUR_TELEGRAM_BOT_TOKEN"

# Image generation function
def generate_image(prompt, width=1024, height=1024, seed=42, model='flux'):
    image_url = f"https://pollinations.ai/p/{requests.utils.quote(prompt)}?width={width}&height={height}&seed={seed}&model={model}"
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        return image_url  # Return direct URL instead of downloading
    except Exception as e:
        print("Error:", e)
        return None

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Send me any prompt, and I’ll generate an AI image for you.")

# Text message handler
async def handle_prompt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = update.message.text
    await update.message.reply_text("Generating your image... Please wait")
    image_url = generate_image(prompt)
    if image_url:
        await update.message.reply_photo(photo=image_url, caption=f"Prompt: {prompt}")
    else:
        await update.message.reply_text("Failed to generate image.")

# Main function to launch bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_prompt))
    print("Telegram bot is running...")
    app.run_polling()
