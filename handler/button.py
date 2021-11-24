from aiogram.types.reply_keyboard import KeyboardButton
from aiogram.types import ReplyKeyboardMarkup

btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn.add("🇺🇸Dollar//🇸🇱So'm", "🇸🇱So'm//🇺🇸Dollar", '🇺🇸Dollar//🇷🇺Rubl', "🇷🇺Rubl//🇺🇸Dollar", "🇷🇺Rubl//🇸🇱So'm", "🇸🇱So'm//🇷🇺Rubl")

