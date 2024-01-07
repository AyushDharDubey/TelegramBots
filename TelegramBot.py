import logger
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from telegram import Update, ForceReply


async def start(self, update: Update, context:ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text('fuck')

app = Application.builder().token('6111096637:AAFHqWnDHn371VSRhedmEhpB5_DPlHUejSQ').build()
app.add_handler(CommandHandler('start', start))
app.run_polling()