import os
import sys
import asyncio 
import datetime
import psutil
from pyrogram.types import Message
from database import db, mongodb_version
from config import Config, temp
from platform import python_version
from translation import Translation
from pyrogram import Client, filters, enums, __version__ as pyrogram_version
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaDocument

# Grandpa's Wise Buttons 👴
main_buttons = [[
        InlineKeyboardButton('🧐 ʜᴇʟᴘ, ᴍʏ ᴅᴇᴀʀ', callback_data='help')
        ],[
        InlineKeyboardButton('👴 ɢʀᴀɴᴅᴘᴀ\'s ᴄᴏᴍᴍᴜɴɪᴛʏ', url='https://t.me/Silicon_Botz'),
        InlineKeyboardButton('📰 ɴᴇᴡs ʙᴏᴀʀᴅ', url='https://t.me/Silicon_Bot_Update')
        ],[
        InlineKeyboardButton('💰 sᴜᴘᴘᴏʀᴛ ᴍʏ ᴄᴀʀᴇɢɪᴠᴇʀ', callback_data='donate')
        ]]

#===================Start Function===================#

@Client.on_message(filters.private & filters.command(['start']))
async def start(client, message):
    user = message.from_user
    if Config.FORCE_SUB_ON:
        try:
            member = await client.get_chat_member(Config.FORCE_SUB_CHANNEL, user.id)
            if member.status == "kicked":
                await client.send_message(
                    chat_id=message.chat.id,
                    text="🚫 Oh dear, you've been barred from my little digital world! Must have been some misunderstanding...",
                )
                return
        except:
            # Send a message asking the user to join the channel
            join_button = [
                [InlineKeyboardButton("🤝 ᴊᴏɪɴ ᴍʏ ᴄɪʀᴄʟᴇ", url=f"{Config.FORCE_SUB_CHANNEL}")],
                [InlineKeyboardButton("↻ ʟᴇᴛ ᴍᴇ ᴛʀʏ ᴀɢᴀɪɴ", url=f"https://t.me/{client.username}?start=start")]
            ]
            await client.send_message(
                chat_id=message.chat.id,
                text="🧓 Now listen here, young one. You'll need to join our cozy little channel before we can chat!",
                reply_markup=InlineKeyboardMarkup(join_button)
            )
            return

    if not await db.is_user_exist(user.id):
        await db.add_user(user.id, message.from_user.mention)
        await client.send_message(
            chat_id=Config.LOG_CHANNEL,
            text=f"#NewVisitor\n\nA fresh face has wandered into my digital parlor!\nIᴅ - {user.id}\nNᴀᴍᴇ - {message.from_user.mention}"
        )
    reply_markup = InlineKeyboardMarkup(main_buttons)
    await client.send_message(
        chat_id=message.chat.id,
        reply_markup=InlineKeyboardMarkup(main_buttons),
        text=f"Well, hello there, {message.from_user.first_name}! 👴 Let this old-timer help you navigate this newfangled technology. What can I do for you today?"
    )

#==================Restart Function==================#

@Client.on_message(filters.private & filters.command(['restart']) & filters.user(Config.BOT_OWNER_ID))
async def restart(client, message):
    msg = await message.reply_text(
        text="🕰️ Let me dust off my gears and restart... Give an old man a moment!"
    )
    await asyncio.sleep(5)
    await msg.edit("✅ Phew! All systems back to working order. These young machines, always needing a little tune-up!")
    os.execl(sys.executable, sys.executable, *sys.argv)
    
#==================Callback Functions==================#

@Client.on_callback_query(filters.regex(r'^help'))
async def helpcb(bot, query):
    await query.message.edit_text(
        text="🧓 Oh, you need some guidance! Here's how this old brain can assist you, young one...",
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('• ʜᴏᴡ ᴅᴏᴇs ᴛʜɪs ᴄᴏɴᴛʀᴀᴘᴛɪᴏɴ ᴡᴏʀᴋ? ❓', callback_data='how_to_use')
            ],[
            InlineKeyboardButton('• ᴍʏ ᴄʟᴜᴛᴛᴇʀᴇᴅ sᴇᴛᴛɪɴɢs ', callback_data='settings#main'),
            InlineKeyboardButton('• ᴍʏ ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛᴜs ', callback_data='status')
            ],[
            InlineKeyboardButton('• ɢᴏ ʙᴀᴄᴋ', callback_data='back'),
            InlineKeyboardButton('• ᴀʙᴏᴜᴛ ᴍᴇ', callback_data='about')
            ]]
        ))

@Client.on_callback_query(filters.regex(r'^how_to_use'))
async def how_to_use(bot, query):
    await query.message.edit_text(
        text="🤓 Let me explain this contraption, just like I used to explain things to my grandkids...",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('• ʙᴀᴄᴋ ᴛᴏ sᴀғᴇᴛʏ', callback_data='help')]]),
        disable_web_page_preview=True
    )

@Client.on_callback_query(filters.regex(r'^back'))
async def back(bot, query):
    reply_markup = InlineKeyboardMarkup(main_buttons)
    await query.message.edit_text(
       reply_markup=reply_markup,
       text=f"Back to my digital living room, {query.from_user.first_name}! 👴")

@Client.on_callback_query(filters.regex(r'^about'))
async def about(bot, query):
    await query.message.edit_text(
        text="🕯️ A little story about this old bot... Sit down and let me tell you!",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('• ʙᴀᴄᴋ ʜᴏᴍᴇ', callback_data='back')]]),
        disable_web_page_preview=True,
        parse_mode=enums.ParseMode.HTML,
    )

@Client.on_callback_query(filters.regex(r'^donate'))
async def donate(bot, query):
    await query.message.edit_text(
        text="💸 Ah, thinking of supporting an old man's digital adventures? How kind of you!",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('• ʙᴀᴄᴋ ʜᴏᴍᴇ', callback_data='back')]]),
        disable_web_page_preview=True,
        parse_mode=enums.ParseMode.HTML,
    )

START_TIME = datetime.datetime.now()

# Function to calculate and format bot uptime
def format_uptime():
    uptime = datetime.datetime.now() - START_TIME
    total_seconds = uptime.total_seconds()

    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    uptime_components = []
    if int(days) > 0:
        uptime_components.append(f"{int(days)} D" if int(days) == 1 else f"{int(days)} D")
    if int(hours) > 0:
        uptime_components.append(f"{int(hours)} H" if int(hours) == 1 else f"{int(hours)} H")
    if int(minutes) > 0:
        uptime_components.append(f"{int(minutes)} M" if int(minutes) == 1 else f"{int(minutes)} M")
    if int(seconds) > 0:
        uptime_components.append(f"{int(seconds)} Sec" if int(seconds) == 1 else f"{int(seconds)} Sec")

    uptime_str = ', '.join(uptime_components)
    return uptime_str

@Client.on_callback_query(filters.regex(r'^status'))
async def status(bot, query):
    users_count, bots_count = await db.total_users_bots_count()
    total_channels = await db.total_channels()

    # Calculate bot uptime
    uptime_str = format_uptime()

    await query.message.edit_text(
        text="🧓 Let me tell you about my digital journey...\n\n" + 
             f"Total visitors to my digital porch: {users_count} 👥\n" +
             f"Mechanical helpers: {bots_count} 🤖\n" +
             f"Channels I'm keeping an eye on: {total_channels} 📺",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton('• ʙᴀᴄᴋ ʜᴏᴍᴇ', callback_data='help'),
            InlineKeyboardButton('• sᴇʀᴠᴇʀ ʜᴇᴀʟᴛʜ', callback_data='server_status')
        ]]),
        parse_mode=enums.ParseMode.HTML,
        disable_web_page_preview=True,
    )

@Client.on_callback_query(filters.regex(r'^server_status'))
async def server_status(bot, query):
    ram = psutil.virtual_memory().percent
    cpu = psutil.cpu_percent()

    await query.message.edit_text(
        text=f"🩺 My digital health report:\n\n" +
             f"Brain activity (CPU): {cpu}% 🧠\n" +
             f"Energy levels (RAM): {ram}% 🔋",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('• ʙᴀᴄᴋ ᴛᴏ ʀᴇᴘᴏʀᴛ', callback_data='status')]]),
        parse_mode=enums.ParseMode.HTML,
        disable_web_page_preview=True,
    )

#===================Donate Function===================#

@Client.on_message(filters.private & filters.command(['donate']))
async def restart(client, message):
    msg = await message.reply_text(
        text="🤵 Ah, my dear young friend! If you found my services as comforting as my old rocking chair ❤️\n\n" +
             "Consider supporting this elderly fellow's caregiver. Every little bit helps an old man keep his tech running! 👴\n\n" +
             "My digital coin purse ID - `pay-to-yash-singh@fam`"
    )
