from aiogram import Bot, Dispatcher


ADMINS = [908379438, 5517017632]
COINGECKO_API_URL = 'https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd'
TOKEN = "6466756485:AAG39gvPwH1gjdnSuGE3Ym6oz7AOCqAZ9OY"
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot=bot)
