import os

from dotenv import load_dotenv
from telethon import TelegramClient, events
from telethon.tl.types import Channel

from normalize_id import normalize_id

load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient("mirror", api_id, api_hash)

main_channel_id = normalize_id(int(os.getenv("MAIN_CHANNEL_ID")))


async def get_channels():
    channels = [
        dialog.id
        for dialog in (await client.get_dialogs())
        if isinstance(dialog.entity, Channel) and dialog.id != main_channel_id
    ]

    return channels


async def forward_message(event):
    await client.forward_messages(main_channel_id, event.message)

    await client.send_read_acknowledge(event.chat_id)  # Read the messages


async def main():
    channels = await get_channels()

    client.add_event_handler(forward_message, events.NewMessage(chats=channels))

    await client.run_until_disconnected()


if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())
