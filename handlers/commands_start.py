import asyncio
import random

from misc import dp,bot
from .sqlit import reg_user,cheak_linkss
from aiogram import types

channels = -1001750636180
l = "https://t.me/share/url?url=https%3A%2F%2Ft.me%2F%2B"
reposts = [f"{l}HHl96dMvADVlZmFi"]

content_id = -1001165606914

async def posting():
    while True:
        try:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Share to open 💬', url=reposts[0])
            markup.add(bat_a)
            q = await bot.copy_message(chat_id=channels,from_chat_id=content_id,message_id=19,reply_markup=markup)
        except:
            pass


        await asyncio.sleep(60)

        try:
            await bot.delete_message(chat_id=channels,message_id=q.message_id)
        except:
            pass




@dp.chat_join_request_handler()
async def join(update: types.ChatJoinRequest):
    reg_user(update.from_user.id,1)
    if update.chat.id == channels:
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='Share to open 💬', url=reposts[0])
        markup.add(bat_a)
        await bot.copy_message(chat_id=update.from_user.id, from_chat_id=content_id, message_id=20)
        try:
            await update.approve()
        except:
            pass
        await asyncio.sleep(1200)
        await bot.copy_message(chat_id=update.from_user.id, from_chat_id=content_id, message_id=20)

        await asyncio.sleep(1200)
        try:
            await bot.send_message(chat_id=update.from_user.id, text=f"""<b>Hi {update.from_user.first_name} 👋
⚙️You shared a link 2/3
🆔Your ID 943222567 👈</b>

<i>Share the link 1 time and I will give you access 👇👇👇</i>""",reply_markup=markup)
        except:
            pass

        await asyncio.sleep(1200)
        try:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text="JOIN THE GROUP", url="https://t.me/+6wifEv8tuppiMDhi")
            markup.add(bat_a)

            await bot.send_message(chat_id=update.from_user.id, text=f"""<b>Access is open ✅</b>""", reply_markup=markup)
        except:
            pass




@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='Share to open 💬', url=reposts[0])
    markup.add(bat_a)
    print(message.chat.id)
    q = await bot.copy_message(chat_id=message.chat.id,from_chat_id=content_id,message_id=20,reply_markup=markup)