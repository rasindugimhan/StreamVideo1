import asyncio
from pyrogram import Client, filters
from helper.bot_utils import USERNAME
from pyrogram.errors import BotInlineDisabled
from config import API_ID, API_HASH, SESSION_STRING, REPLY_MESSAGE


User = Client(
    SESSION_STRING,
    API_ID,
    API_HASH
)

@User.on_message(filters.private & filters.incoming & ~filters.bot & ~filters.service & ~filters.me & ~filters.edited & ~filters.chat([777000, 454000]))
async def nopm(client, message):
    if REPLY_MESSAGE is not None:
        try:
            inline = await client.get_inline_bot_results(USERNAME, "SAF_ONE")
            await client.send_inline_bot_result(
                message.chat.id,
                query_id=inline.query_id,
                result_id=inline.results[0].id,
                hide_via=True
            )
        except BotInlineDisabled:
            print(f"[WARN] - Inline Mode for @{USERNAME} is not enabled. Enable from @Botfather to enable PM Permit !")
            await message.reply_text(f"{REPLY_MESSAGE}\n\n<b>© Powered By : \n@AsmSafone | @SafoTheBot 👑</b>")
        except Exception as e:
            print(e)
            pass
