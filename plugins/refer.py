from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
@Client.on_message(filters.private & filters.command(["refer"]))
async def refer(client,message):
    reply_markup = InlineKeyboardMarkup(
       		[ [ InlineKeyboardButton("Share Your Link" ,url=f"https://t.me/share/url?url=https://t.me/rename_urbot?start={message.from_user.id}") ]   ])
    await message.reply_text(f"Refer And Earn Get 100MB Upload Limit\nPer Refer 100MB\n Your Link :- https://t.me/rename_urbot?start={message.from_user.id} ",reply_to_message_id = message.id,reply_markup=reply_markup,)
    
