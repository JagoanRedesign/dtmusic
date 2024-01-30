from pyrogram import filters
from pyrogram.types import Message
from DAXXMUSIC.plugins.tools.pretenderdb import impo_off, impo_on, check_pretender, add_userdata, get_userdata, usr_data
from DAXXMUSIC import app




@app.on_message(filters.group & ~filters.bot & ~filters.via_bot, group=69)
async def chk_usr(_, message: Message):
    if message.sender_chat or not await check_pretender(message.chat.id):
        return
    if not await usr_data(message.from_user.id):
        return await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    usernamebefore, first_name, lastname_before = await get_userdata(message.from_user.id)
    msg = ""
    if (
        usernamebefore != message.from_user.username
        or first_name != message.from_user.first_name
        or lastname_before != message.from_user.last_name
    ):
        msg += f"""Saya melihat **{message.from_user.mention}** merubah :"""
    if usernamebefore != message.from_user.username:
        usernamebefore = f"@{usernamebefore}" if usernamebefore else "NO USERNAME"
        usernameafter = (
            f"@{message.from_user.username}"
            if message.from_user.username
            else "NO USERNAME"
        )
        msg += """\nUsername dari <b>{bef}</b> menjadi <b>{aft}</b>""".format(bef=usernamebefore, aft=usernameafter)
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if first_name != message.from_user.first_name:
        msg += """\nNama depan dari <b>{bef}</b> menjadi <b>{aft}</b>""".format(
            bef=first_name, aft=message.from_user.first_name
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if lastname_before != message.from_user.last_name:
        lastname_before = lastname_before or "NO LAST NAME"
        lastname_after = message.from_user.last_name or "NO LAST NAME"
        msg += """\nNama belakang dari <b>{bef}</b> menjadi <b>{aft}</b>""".format(
            bef=lastname_before, aft=lastname_after
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if msg != "":
        await message.reply(msg)



@app.on_message(filters.group & filters.command("imposter") & ~filters.bot & ~filters.via_bot)
async def set_mataa(_, message: Message):
    if len(message.command) == 1:
        return await message.reply("**ᴅᴇᴛᴇᴋꜱɪ ᴩᴇɴɢɢᴜɴᴀᴀɴ ᴩʀᴇᴛᴇɴᴅᴇʀ : ᴩʀᴇᴛᴇɴᴅᴇʀ ᴏɴ|ᴏғғ**")
    if message.command[1] == "on":
        cekset = await impo_on(message.chat.id)
        if cekset:
            await message.reply("**ᴍᴏᴅᴇ ᴩʀᴇᴛᴇɴᴅᴇʀ ꜱᴜᴅᴀʜ ᴅɪᴀᴋᴛɪғᴋᴀɴ.**")
        else:
            await impo_on(message.chat.id)
            await message.reply(f"**ᴍᴏᴅᴇ ᴩʀᴇᴛᴇɴᴅᴇʀ ʙᴇʀʜᴀꜱɪʟ ᴅɪᴀᴋᴛɪғᴋᴀɴ ᴜɴᴛᴜᴋ** {message.chat.title}")
    elif message.command[1] == "off":
        cekset = await impo_off(message.chat.id)
        if not cekset:
            await message.reply("**ᴍᴏᴅᴇ ᴩʀᴇᴛᴇɴᴅᴇʀ ꜱᴜᴅᴀʜ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ.**")
        else:
            await impo_off(message.chat.id)
            await message.reply(f"**ᴍᴏᴅᴇ ᴩʀᴇᴛᴇɴᴅᴇʀ ʙᴇʀʜᴀꜱɪʟ ᴅᴏɴᴀᴋᴛɪғᴋᴀɴ ᴜɴᴛᴜᴋ** {message.chat.title}")
    else:
        await message.reply("**ᴅᴇᴛᴇᴋꜱɪ ᴩᴇɴɢɢᴜɴᴀᴀɴ ᴩʀᴇᴛᴇɴᴅᴇʀ : ᴩʀᴇᴛᴇɴᴅᴇʀ ᴏɴ|ᴏғғ**")
