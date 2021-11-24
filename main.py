import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import CommandStart
import datetime as t
import requests
# import API.exchangeAPI as data
from aiogram.types import ReplyKeyboardMarkup

btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn.add("🇺🇸Dollar//🇸🇱So'm", "🇸🇱So'm//🇺🇸Dollar", '🇺🇸Dollar//🇷🇺Rubl', "🇷🇺Rubl//🇺🇸Dollar", "🇷🇺Rubl//🇸🇱So'm", "🇸🇱So'm//🇷🇺Rubl")


API_TOKEN = '2105356595:AAG-Ebw70bBrFjlhqELPD5rfL_NPk-fSOhE'
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(CommandStart())
async def handlarlars(message: types.Message):
    await message.answer(f"Assalomu aleykum hurmat talab inson {message.from_user.full_name}. Sizni botimizda ko'rib turganimizda hursandmiz", reply_markup=btn)


# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     """
#     This handler will be called when user sends `/start` or `/help` command
#     """

@dp.message_handler(content_types="text")
async def dollor(message: types.Message):
    enter = 'USD'
    exits = 'UZS'
    money = 'dollar'
    exiting = "so'm"
    text = message.text
    if text == "🇺🇸Dollar//🇸🇱So'm":
        enter = "USD"
        exits = "UZS"
        money = 'dollar'
        exiting = "so'm"
    if text == "🇸🇱So'm//🇺🇸Dollar":
        enter = "UZS"
        exits = "USD"
        money = "so'm"
        exiting = "dollar"
    if text == "🇺🇸Dollar//🇷🇺Rubl":
        enter = "USD"
        exits = "RUB"
        money = 'dollor'
        exiting = "rubl"
    if text == "🇷🇺Rubl//🇺🇸Dollar":
        enter = 'RUB'
        exits = "USD"
        money = "rubl"
        exiting = "dollar"
    if text == "🇸🇱So'm//🇷🇺Rubl":
        enter = "UZS"
        exits = "RUB"
        money = "so'm"
        exiting = "rubl"
    if text == "🇷🇺Rubl//🇸🇱So'm":
        enter = "RUB"
        exits = "UZS"
        money = "rubl"
        exiting = "so'm"


    # Where USD is the base currency you want to use
    url = f'https://v6.exchangerate-api.com/v6/f4c3988ec1b2915571fc66f8/pair/{enter}/{exits}'
    # Making our request
    response = requests.get(url)
    data = response.json()
    # qiymat = round(data["conversion_rate"])
    # butun = str(qiymat // 1000)
    # qoldiq = str(qiymat % 1000)
    time = t.datetime.now()
    year = time.strftime("%Y")
    day = time.strftime("%d")
    month = time.strftime("%m")
    qiymayt = data["conversion_rate"]
    await message.answer(f"⏰{year}.{day}.{month}kungi hisobotgaq ko'ra\n💵1 {money} = {qiymayt} {exiting}\n\n Created by Suhrob Mavlonov")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)