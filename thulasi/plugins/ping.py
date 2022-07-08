import os

from telethon import Button, events

from thulasi import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/1aaf04b524b231ae0d7b1.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@KANTHARI_WRITINGS"
)

CAPTION = f"**꧁•⊹٭Ping٭⊹•꧂**\n\n   ⚜ {ms}\n   ⚜ ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『{ALIVE}』"


@thulasi.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    UMM = [[Button.url("⚜ Cԋαɳɳҽʅ ⚜", "https://t.me/stenzle_appealchat")]]
    await thulasi.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
