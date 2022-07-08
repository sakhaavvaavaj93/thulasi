from thulasi import thulasi, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
🥀നമസ്കാരം🎻 {}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
𝙸 𝚊𝚖 𝚊 𝚕𝚊𝚐𝚐𝚕𝚎𝚜𝚜 𝚖𝚞𝚜𝚒𝚌 𝚋𝚘𝚝 𝚌𝚛𝚎𝚊𝚝𝚎𝚍 𝚏𝚘𝚛 [കണിമംഗലം](https://t.me/kk_kovilakam)
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
💎 𝙵𝚘𝚛 𝚊𝚍𝚍 𝚝𝚑𝚒𝚜 𝙱𝚘𝚝
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
𝑪𝒐𝒏𝒕𝒂𝒄𝒕 : [𝐎𝐰𝐧𝐞𝐫](https://t.me/kk_heavenhater)

"""

@thulasi.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("🖌️ എഴുത്ത് പുര 🥀", f"https://t.me/KANTHARI_WRITINGS")],
        [Button.inline("ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅꜱ", data="help")]])
       return

    if event.is_group:
       await event.reply("**ʜᴇʏ! ɪ'ᴍ ꜱᴛɪʟʟ ᴀʟɪᴠᴇ ✅**")
       return



@thulasi.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("എഴുത്തുപുര", f"https://t.me/KANTHARI_WRITINGS")],
        [Button.inline("ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅꜱ", data="help")]])
       return
