import asyncio 
from .info import * 
from time import time 
from .database import *
from pyrogram import Client, idle 
#-------------------------------------------------------------------------------
bot = Client("auto-delete-bot",
          api_id=API_ID,
          api_hash=API_HASH,
          bot_token=BOT_TOKEN)
#-------------------------------------------------------------------------------
START_MSG = "<b>Hai {},\nI'm a private bot of @mh_world to delete group messages after a specific time</b>"

async def check_up(bot):   
    _time = int(time()) 
    all_data = get_all_data(_time)
    for data in all_data:
        try:
           await bot.delete_messages(chat_id=data["chat_id"],
                               message_ids=data["message_id"])           
        except Exception as e:
           err=data
           err["Error"]=str(e)
           print(err)
    delete_all_data(all_data)
          
@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))
          
async def run_check_up():
    async with bot:     
        while True:  
           await check_up(bot)
           await asyncio.sleep(1)
    
if __name__=="__main__":   
   asyncio.run(run_check_up())
