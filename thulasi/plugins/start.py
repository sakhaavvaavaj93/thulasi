from thulasi import thulasi, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
๐ฅเดจเดฎเดธเตเดเดพเดฐเด๐ป {}
โโโโโโโโโโโโโโ
๐ธ ๐๐ ๐ ๐๐๐๐๐๐๐๐ ๐๐๐๐๐ ๐๐๐ ๐๐๐๐๐๐๐ ๐๐๐ [เดเดฃเดฟเดฎเดเดเดฒเด](https://t.me/kk_kovilakam)
โโโโโโโโโโโโโโ
๐ ๐ต๐๐ ๐๐๐ ๐๐๐๐ ๐ฑ๐๐
โโโโโโโโโโโโโโ
๐ช๐๐๐๐๐๐ : [๐๐ฐ๐ง๐๐ซ](https://t.me/kk_heavenhater)

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
        [Button.url("โ แดแดแด แดแด แดแด สแดแดส แดสแดแด", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("๐๏ธ เดเดดเตเดคเตเดคเต เดชเตเดฐ ๐ฅ", f"https://t.me/KANTHARI_WRITINGS")],
        [Button.inline("สแดสแด แดษดแด แดแดแดแดแดษดแด๊ฑ", data="help")]])
       return

    if event.is_group:
       await event.reply("**สแดส! ษช'แด ๊ฑแดษชสส แดสษชแด แด โ**")
       return



@thulasi.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("โ แดแดแด แดแด แดแด สแดแดส แดสแดแด", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("เดเดดเตเดคเตเดคเตเดชเตเดฐ", f"https://t.me/KANTHARI_WRITINGS")],
        [Button.inline("สแดสแด แดษดแด แดแดแดแดแดษดแด๊ฑ", data="help")]])
       return
