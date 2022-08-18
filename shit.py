from pyrogram import Client
import pyrogram


def main():
    api_id = 12503964
    api_hash = '7f6f3c9d695c8f1697d69f2466216d42'
    phone_number = '+380666037197'
    masha_chat_id = -1001621051079
    svolota_id = -1001762078325


    client = Client('me7', api_id=api_id, api_hash=api_hash)

    @client.on_message()
    def message_handler(client: pyrogram.Client, message: pyrogram.types.Message):
        if message.chat.id in [svolota_id, masha_chat_id]:
            client.send_reaction(message.chat.id, message.id, '💩')
        client.send_message(svolota_id, f'title: {message.chat.title}\n'
                                        f' name: {message.chat.first_name},'
                                        f' {message.chat.last_name}\n'
                                        f' message: {message.text}')

    client.run()


if __name__ == "__main__":
    main()
