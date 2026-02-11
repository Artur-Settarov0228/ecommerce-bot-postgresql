from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from app.core.session import SessionLocal
from app.services.user_service import UserService
from app.bot.keyboards.main_menu import main_menu_keyboard


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tg_user = update.effective_user

    with SessionLocal() as db:
        UserService.get_or_create(
            db=db,
            telegram_id=tg_user.id,
            full_name=tg_user.full_name or "No name",
        )

    await update.message.reply_text(
        text=(
            "👋 Xush kelibsiz!\n\n"
            "🛒 Bizning e-commerce botimiz orqali "
            "mahsulotlarni ko‘rib, buyurtma berishingiz mumkin."
        ),
        reply_markup=main_menu_keyboard(),
    )


start_handler = CommandHandler("start", start)
