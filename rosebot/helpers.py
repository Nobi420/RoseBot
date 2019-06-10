from pyrogram import Message

# Code stolen from: https://git.colinshark.de/PyroBot/PyroBot/src/branch/develop/pyrobot/modules/memes.py
# -- Helpers -- #
def ReplyCheck(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.message_id

    elif not message.from_user.is_self:
        reply_id = message.message_id

    return reply_id


# -- Helpers End -- #
