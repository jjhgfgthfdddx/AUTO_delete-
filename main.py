from time import time 
from utils.info import *
from subprocess import Popen
from pyrogram import Client, filters

User = Client("auto-delete-user",
              session_string=SESSION)

@User.on_message()
async def delete(user, message):
  await message.delete()

@User.on_message(filters.regex("!start") & filters.private)
async def start(user, message):
    await message.reply("Hi, I'm alive!")

#==========================================================

Popen(f"gunicorn utils.server:app --bind 0.0.0.0:{PORT}", shell=True)
User.run()
