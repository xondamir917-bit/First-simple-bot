from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

async def start(update: Update, context):
    await update.message.reply_text("Good morning. How are you?\nMy commands:\n/start - New message\n/help - My self")

async def help(update: Update, context):
    await update.message.reply_text("My self. My name is Simple bot.")

async def echo(update: Update, context):
    await update.message.reply_text(update.message.text)

app = Application.builder().token("Bot_token_here").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))


app.run_polling()
