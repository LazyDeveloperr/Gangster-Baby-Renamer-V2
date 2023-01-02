import os 
from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user
from helper.progress import humanbytes
import pymongo
from helper.date import add_date
DB_NAME = os.environ.get("DB_NAME", "")
DB_URL = os.environ.get("DB_URL", "")
mongo = pymongo.MongoClient(DB_URL)
db = mongo[DB_NAME]
dbcol = db["user"]

def getid():
    values = [].split("\\R", -1)
    for key in dbcol.find():
        id = key["_id"]
        values.append((id))
    return values

@Client.on_message(filters.private & filters.command(["alluser"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"{getid()}\n Total User :- {total_user()}\n\nTotal Renamed File :- {total_rename}\nTotal Size Renamed :- {humanbytes(int(total_size))}",quote=True,
                             reply_markup= InlineKeyboardMarkup([[InlineKeyboardButton("🦋 Close Menu 🦋", callback_data="cancel")]]) 
                             )
