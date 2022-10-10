from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor



#from config import TOKEN


bot = Bot(token="5297609562:AAFVFLUqY53XWDnMAfX0e1JsVyatwDIeq1I")
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")

print(1)
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")



@dp.message_handler(commands=['Лох!'])
async def echo_message(message: types.Message):
    await bot.send_message(message.from_user.id,"Сам такой!")
@dp.message_handler()
async def echo_message(msg: types.Message):
    if msg.text=="Абоба":
        await bot.send_message(msg.from_user.id, "!")
    else:

        await bot.send_message(msg.from_user.id, msg.text)

executor.start_polling(dp)