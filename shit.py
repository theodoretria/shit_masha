from pyrogram import Client
import pyrogram

from pyrogram.raw.functions.messages import GetMessageReactionsList
import pandas as pd

import asyncio
import os
from winsound import Beep
import sys

def main():
    api_id = int(sys.argv[1])
    api_hash = sys.argv[2]
    masha_chat_id = -1001621051079
    svolota_id = -1001762078325

    client = Client('me7', api_id=api_id, api_hash=api_hash)


    @client.on_message(group=svolota_id)
    async def message_handler(client:pyrogram.Client, message:pyrogram.types.Message):
        if message.chat.id in  [svolota_id, masha_chat_id]:
            await client.send_reaction(message.chat.id, message.id, '💩')


    client.run()

if __name__ == "__main__":
    main()