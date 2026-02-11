from telegram.ext import ApplicationBuilder

from app.core.config import settings
from app.bot.handlers.start import start_handler
from app.bot.handlers.menu import menu_message_handler


def create_app():
    app = (
        ApplicationBuilder()
        .token(settings.TOKEN)
        .build()
    )

    app.add_handler(start_handler)
    app.add_handler(menu_message_handler)

    return app
