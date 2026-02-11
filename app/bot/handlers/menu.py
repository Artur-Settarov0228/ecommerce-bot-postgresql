from telegram import Update
from telegram.ext import MessageHandler, ContextTypes, filters


async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🛒 Mahsulotlar":
        await update.message.reply_text(
            "📦 Mahsulotlar ro‘yxati yuklanmoqda..."
        )

    elif text == "🧺 Savatcha":
        await update.message.reply_text(
            "🧺 Savatchangiz hozircha bo‘sh."
        )

    elif text == "ℹ️ Biz haqimizda":
        await update.message.reply_text(
            "ℹ️ Biz — sifatli mahsulotlar sotuvchi do‘konmiz."
        )


menu_message_handler = MessageHandler(
    filters.TEXT & ~filters.COMMAND,
    menu_handler,
)
