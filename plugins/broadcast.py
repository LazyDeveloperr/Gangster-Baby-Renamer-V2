import os
from pyrogram.errors import FloodWait
import asyncio
from pyrogram import Client, filters
from helper.database import getid, delete
import time
ADMIN = int(os.environ.get("ADMIN", 1484670284))


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
    if (message.reply_to_message):
        ms = await message.reply_text("Geting All ids from database..\n Please wait")
        ids = getid()
        tot = len(ids)
        success = 0
        failed = 0
        await ms.edit(f"Starting Broadcast... \n Sending Message To {tot} Users")
        for id in ids:
            try:
                time.sleep(1)
                await message.reply_to_message.copy(id)
                success += 1
            except:
                failed += 1
                delete({"_id": id})
                pass
            try:
                await ms.edit(f"Message sent to {success} chat(s). {failed} chat(s) failed on receiving message. \nTotal - {tot}")
            except FloodWait as e:
                await asyncio.sleep(t.x)


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["alluser"]))
async def alluser(bot, message):
    if (alluser):
        ids = getid()
        tot = len(ids)
        await message.reply_text(text=f"Sending Message To {id} Users")
        for id in ids:
            try:
                await message.reply_text(text=f"Id:{id} \nTotal - {tot}")
            except FloodWait as e:
                await asyncio.sleep(t.x)
            return
