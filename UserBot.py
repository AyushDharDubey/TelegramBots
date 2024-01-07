import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

from telethon import TelegramClient, events

client = TelegramClient('UserBot', 25190027, 'c16d46ef158597cd68340ae2a0884f2f')

@client.on(events.NewMessage(outgoing=True, pattern=r'._save'))
async def save_msg_without_frwd_tag(event):
    if event.is_reply:
        replied = await event.get_reply_message()
        await client.send_message('me', replied)
        await event.delete()

@client.on(events.NewMessage(outgoing=True, pattern=r'.save'))
async def save_msg(event):
    if event.is_reply:
        replied = await event.get_reply_message()
        await client.forward_messages('me', replied)
        await event.delete()

with client:
    client.start()
    client.run_until_disconnected()