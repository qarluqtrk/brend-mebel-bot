from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def main_brand_inline_button():
    rkm = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn = InlineKeyboardButton(text="👤 Ro'yxatdan o'tish", callback_data="register")
    btn2 = InlineKeyboardButton(text="✍️ Fikr bildirish", callback_data="idea")
    btn3 = InlineKeyboardButton(text="🏬 Biz haqimizda", callback_data="about")
    btn4 = InlineKeyboardButton(text="🪑 Buyurtma berish", callback_data="order")
    rkm.add(btn, btn2, btn3, btn4)
    return rkm


def main_menu_back():
    rkm = InlineKeyboardMarkup(resize_keyboard=True)
    btn = InlineKeyboardButton(text="⬅️ Asosiy menu", callback_data="main_menu")
    rkm.add(btn)
    return rkm
