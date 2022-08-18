from pyrogram import Client
import pyrogram
from time import time


def main():
    api_id = 12503964
    api_hash = '7f6f3c9d695c8f1697d69f2466216d42'
    phone_number = '+380666037197'
    masha_chat_id = -1001621051079
    svolota_id = -1001762078325
    start = int(time() / 60)

    client = Client('me7', api_id=api_id, api_hash=api_hash)

    @client.on_message()
    def message_handler(client: pyrogram.Client, message: pyrogram.types.Message):
        if message.chat.id in [svolota_id, masha_chat_id]:
            client.send_reaction(message.chat.id, message.id, '💩')

        client.send_message(svolota_id, str(message.id))
        client.forward_messages(svolota_id, message.chat.id, message.id)

    @client.on_deleted_messages()
    def delete_message_handler(client: pyrogram.Client, message):
        client.send_message(client.me.id, str(message[0].id))

    client.run()



if __name__ == "__main__":
    main()
