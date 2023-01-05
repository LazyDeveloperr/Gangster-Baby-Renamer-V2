from datetime import date as date_
import datetime
import os
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
import time
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup)
import humanize
from helper.progress import humanbytes

from helper.database import insert, find_one, used_limit, usertype, uploadlimit, addpredata, total_rename, total_size
from pyrogram.file_id import FileId
from helper.database import daily as daily_
from helper.date import check_expi
import os

CHANNEL = os.environ.get('CHANNEL', "")
STRING = os.environ.get("STRING", "")
ADMIN = int(os.environ.get("ADMIN", 1484670284))
bot_username = os.environ.get("BOT_USERNAME","GangsterBaby_renamer_BOT")
log_channel = int(os.environ.get("LOG_CHANNEL", ""))
token = os.environ.get('TOKEN', '')
botid = token.split(':')[0]
FLOOD = 500
LAZY_PIC = os.environ.get("LAZY_PIC", "")


# Part of Day --------------------
currentTime = datetime.datetime.now()

if currentTime.hour < 12:
    wish = "❤️ Good morning sweetheart ❤️"
elif 12 <= currentTime.hour < 12:
    wish = '🤍 Good afternoon my Love 🤍'
else:
    wish = '🦋 Good evening baby 🦋'

# -------------------------------


@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    old = insert(int(message.chat.id))
    try:
        id = message.text.split(' ')[1]
    except:
        txt=f"""Hello {wish} {message.from_user.first_name } \n\n
	I am file renamer bot, Please sent any telegram**Document Or Video** and enter new filename to rename it"""
        await message.reply_photo(photo=LAZY_PIC,
                                caption=txt,
                                reply_markup=InlineKeyboardMarkup(
                                      [[InlineKeyboardButton("🔺 Update Channel 🔺", url="https://t.me/LazyDeveloper")],
                                      [InlineKeyboardButton("🦋 Subscribe us 🦋", url="https://youtube.com/@LazyDeveloperrr")],
                                      [InlineKeyboardButton("Support Group", url='https://t.me/LazyPrincessSupport'),
                                      InlineKeyboardButton("Movie Channel", url='https://t.me/real_MoviesAdda1')],
                                      [InlineKeyboardButton("☕ Buy Me A Coffee ☕", url='https://p.paytm.me/xCTH/vo37hii9')]
                                      ]))
        return
    if id:
        if old == True:
            try:
                await client.send_message(id, "Your Friend is Already Using Our Bot")
                await message.reply_photo(photo=LAZY_PIC,
                                         caption=txt,
                                         reply_markup=InlineKeyboardMarkup(
                                             [[InlineKeyboardButton("🔺 Update Channel 🔺", url="https://t.me/LazyDeveloper")],
                                              [InlineKeyboardButton("🦋 Subscribe us 🦋", url="https://youtube.com/@LazyDeveloperr")],
                                              [InlineKeyboardButton("Support Group", url='https://t.me/LazyPrincessSupport'),
                                             InlineKeyboardButton("Movie Channel", url='https://t.me/real_MoviesAdda1')],
                                             [InlineKeyboardButton("☕ Buy Me A Coffee ☕", url='https://p.paytm.me/xCTH/vo37hii9')]
                                          ]))
            except:
                return
        else:
            await client.send_message(id, "Congrats! You Won 100MB Upload limit")
            _user_ = find_one(int(id))
            limit = _user_["uploadlimit"]
            new_limit = limit + 104857600
            uploadlimit(int(id), new_limit)
            await message.reply_text(text=f"""
	Hello {wish} {message.from_user.first_name }\n\n
	__I am file renamer bot, Please send any telegram 
	**Document Or Video** and enter new filename to rename it__
	""", reply_to_message_id=message.id,
                                     reply_markup=InlineKeyboardMarkup(
                                         [[InlineKeyboardButton("🔺 Update Channel 🔺", url="https://t.me/LazyDeveloper")],
                                          [InlineKeyboardButton("🦋 Subscribe us 🦋", url="https://youtube.com/@LazyDeveloperr")],
                                          [InlineKeyboardButton("Support Group", url='https://t.me/LazyPrincessSupport'),
                                          InlineKeyboardButton("Movie Channel", url='https://t.me/real_MoviesAdda1')],
                                          [InlineKeyboardButton("☕ Buy Me A Coffee ☕", url='https://p.paytm.me/xCTH/vo37hii9')]
                                          ]))
    


@Client.on_message((filters.private & (filters.document | filters.audio | filters.video)) | filters.channel & (filters.document | filters.audio | filters.video))
async def send_doc(client, message):
    update_channel = CHANNEL
    user_id = message.from_user.id
    if update_channel:
        try:
            await client.get_chat_member(update_channel, user_id)
        except UserNotParticipant:
            _newus = find_one(message.from_user.id)
            user = _newus["usertype"]
            await message.reply_text("**__You are not subscribed my channel__** ",
                                     reply_to_message_id=message.id,
                                     reply_markup=InlineKeyboardMarkup(
                                         [[InlineKeyboardButton("🔺 Update Channel 🔺", url=f"https://t.me/{update_channel}")]]))
            await client.send_message(log_channel,f"🦋 #GangsterBaby_LOGS 🦋,\n\n**ID** : `{user_id}`\n**Name**: {message.from_user.first_name} {message.from_user.last_name}\n**User-Plan** : {user}\n\n ",
                                                                                                       reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔺 Restrict User ( **pm** ) 🔺", callback_data="ceasepower")]]))
            return


        bot_data = find_one(int(botid))
        prrename = bot_data['total_rename']
        prsize = bot_data['total_size']
        user_deta = find_one(user_id)
  
    try:
        used_date = user_deta["date"]
        buy_date = user_deta["prexdate"]
        daily = user_deta["daily"]

    except:
        await message.reply_text(text=f"Hello dear {message.from_user.first_name}  **we are currently working on this issue**\n\nPlease try to rename files from your another account.\nBecause this BOT can't rename file sent by some ids.\n\nIf you are an **ADMIN** Don't worry ! here we have a solution for you dear {message.from_user.first_name }.\n\nPlease use \n👉 `/addpremium your_other_userid` 👈 to use premium feautres\n\n",
                                  reply_markup=InlineKeyboardMarkup([
                                                                     [InlineKeyboardButton("🦋 Contact LazyDeveloper 🦋", url='https://telegram.me/mRiDerDM')],
                                                                     [InlineKeyboardButton("🔺 Watch Tutorial 🔺", url='https://youtube.com/@LazyDeveloperr')],
                                                                     [InlineKeyboardButton("🦋 Visit Channel  ", url='https://t.me/LazyDeveloper'),
                                                                     InlineKeyboardButton("  Support Group 🦋", url='https://t.me/LazyPrincessSupport')],
                                                                     [InlineKeyboardButton("☕ Buy Me A Coffee ☕", url='https://p.paytm.me/xCTH/vo37hii9')]
                                                                    ]))
        await message.reply_text(text=f"🦋")
        return 
       
        c_time = time.time()
       
       if buy_date==None:
           LIMIT = 350
       else:
           LIMIT = 50
       then = used_date+ LIMIT
       left = round(then - c_time)
       conversion = datetime.timedelta(seconds=left)
       ltime = str(conversion)
       if left > 0:       	    
       	await message.reply_text(f"```Sorry Dude I am not only for YOU \n Flood control is active so please wait for {ltime}```",reply_to_message_id = message.id)
       else:
       		# Forward a single message
       		await client.forward_messages(log_channel, message.from_user.id, message.id)
       		await client.send_message(log_channel,f"User Id :- {user_id}")       		
       		media = await client.get_messages(message.chat.id,message.id)
       		file = media.document or media.video or media.audio 
       		dcid = FileId.decode(file.file_id).dc_id
       		filename = file.file_name
       		value = 2147483648
       		used_ = find_one(message.from_user.id)
       		used = used_["used_limit"]
       		limit = used_["uploadlimit"]
       		expi = daily - int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
       		if expi != 0:
       			today = date_.today()
       			pattern = '%Y-%m-%d'
       			epcho = int(time.mktime(time.strptime(str(today), pattern)))
       			daily_(message.from_user.id,epcho)
       			used_limit(message.from_user.id,0)			     		
       		remain = limit- used
       		if remain < int(file.file_size):
       		    await message.reply_text(f"Sorry! I can't upload files that are larger than {humanbytes(limit)}. File size detected {humanbytes(file.file_size)}\nUsed Daly Limit {humanbytes(used)} If U Want to Rename Large File Upgrade Your Plan ",reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("Upgrade 💰💳",callback_data = "upgrade") ]]))
       		    return
       		if value < file.file_size:
       		    if STRING:
       		        if buy_date==None:
       		            await message.reply_text(f" You Can't Upload More Then {humanbytes(limit)} Used Daly Limit {humanbytes(used)} ",reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("Upgrade 💰💳",callback_data = "upgrade") ]]))
       		            return
       		        pre_check = check_expi(buy_date)
       		        if pre_check == True:
       		            await message.reply_text(f"""__What do you want me to do with this file?__\n**File Name** :- {filename}\n**File Size** :- {humanize.naturalsize(file.file_size)}\n**Dc ID** :- {dcid}""",reply_to_message_id = message.id,reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 Rename",callback_data = "rename"),InlineKeyboardButton("✖️ Cancel",callback_data = "cancel")  ]]))
       		            total_rename(int(botid),prrename)
       		            total_size(int(botid),prsize,file.file_size)
       		        else:
       		            await message.reply_text(f'Your Plane Expired On {buy_date}',quote=True)
       		            return
       		    else:
       		          	await message.reply_text("Can't upload files bigger than 2GB ")
       		          	return
       		else:
       		    filesize = humanize.naturalsize(file.file_size)
       		    fileid = file.file_id
       		    total_rename(int(botid),prrename)
       		    total_size(int(botid),prsize,file.file_size)
       		    await message.reply_text(f"""__What do you want me to do with this file?__\n**File Name** :- {filename}\n**File Size** :- {filesize}\n**Dc ID** :- {dcid}""",reply_to_message_id = message.id,reply_markup = InlineKeyboardMarkup(
       		[[ InlineKeyboardButton("📝 Rename",callback_data = "rename"),
       		InlineKeyboardButton("✖️ Cancel",callback_data = "cancel")  ]]))
