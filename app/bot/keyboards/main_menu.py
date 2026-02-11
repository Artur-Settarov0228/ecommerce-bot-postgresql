from telegram import ReplyKeyboardMarkup

def main_menu_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            ["🛒 Mahsulotlar"],
            ["🧺 Savatcha"],
            ["ℹ️ Biz haqimizda"],
        ],
        resize_keyboard=True,
        one_time_keyboard=False,
    )
