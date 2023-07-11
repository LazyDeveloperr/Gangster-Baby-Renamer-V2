import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6329010856:AAHbsBwdB_2OaP79PC2U1mbboYuo1NUNvE8")

API_ID = int(os.environ.get("API_ID", "20886519"))

API_HASH = os.environ.get("API_HASH", "200096623fc84f791d07d8b44169b163")

STRING = os.environ.get("STRING", "")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
