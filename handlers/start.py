from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_photo("https://telegra.ph/file/d29f183e61134d4cc7475.jpg")
    await message.reply_text(
        f"""**Hey, I'm ⁪⁬⁮╚»Tᴄ☫Dᴏᴘᴀ«╝Oᴘ♡︎[#5]MUSIC BOT🎵

I can play ꬺᶙȿᶖɕ  in your group's voice CHAT Developed by [⁪⁬⁮╚»Tᴄ☫Dᴏᴘᴀ«╝Oᴘ♡︎](https://t.me/nIkLaUsMiKaElSn)

Add me to your group and play music freely😆!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📠 Source Code 📠", url="https://github.com/tana9373/MARATHA_WARRIOR_MUSIC")
                  ],[
                    InlineKeyboardButton(
                        "📢 SUPPORT GROUP 📢", url="https://t.me/universal_op_chat"
                    ),
                    InlineKeyboardButton(
                        "🔰 COMMAND 🔰", url="https://t.me/MARATH_IWARRIORS/18"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "GROUP ME LEJAO 😆", url="https://t.me/DOPA_OP_MUSIC_BOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**#DOPA_MUSIC_OP_BOLATE**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔰 COMMANDS 🔰", url="https://t.me/MARATH_IWARRIORS/18")
                ]
            ]
        )
   )


