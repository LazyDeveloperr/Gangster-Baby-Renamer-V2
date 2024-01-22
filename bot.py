import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6714999304:AAG2tBby7D4QoIGUhsI5uV0PWxXZThZDyM4")

API_ID = int(os.environ.get("API_ID", "24482734"))

API_HASH = os.environ.get("API_HASH", "5ccf6a58166cc047a7eba01c5dbc930c")

STRING = os.environ.get("STRING", "BQBhHWNbz0S4MJX0CGwRlXwgvEjDHL-v5q7ibdDWKiAbnJhqptW7RQmaS1umTbbSWPZZ60EY6x_exqgVjxombeYkndSrMkQrI9EJha5cI13Ht-Z12Pq32gSm-eQsGJHACi5ztCwNDZeFhl8NfLOHwjoH7AjklBQ3o6XvZkn5sDmFEGpPeSIY4g3N50wt26b9pim2_VUjEBy4dOnDJYvTIPkvmI7Qa6qA6yKUVsgSkvXhmL5uoXUsUq5UpTyIswnEp_LNTmcYstcaHeEgP7s2OTiXQaM5xF5UBg5raPWwcJvuISEzM87SeQGm9pJL9ztemMpEiAzSILNZU69SjaBgn_ATar0RrQA")



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
