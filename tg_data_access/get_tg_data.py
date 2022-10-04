from telethon.client import TelegramClient
import json

channels = ['https://t.me/rian_ru', 'rbc_news'] # URL or tg name
api_id = ''                             # From https://my.telegram.org/
api_hash = ''

client = TelegramClient('test_session',
                    api_id,
                    api_hash)
client.start()
all_messages = {}
async def main():
    for channel in channels:
        channel_entity= await client.get_entity(channel)
        messages = await client.get_messages(channel_entity, limit=100)
        all_messages[channel] = []
        for x in messages:
            msg = {
                'message': x.message,
                'date': x.date.timestamp(),
                'views': x.views,
                'forwards': x.forwards,
                # 'reactions': x.reactions
            }
            all_messages[channel].append(msg)


with client:
    client.loop.run_until_complete(main())
res = json.dumps(all_messages, ensure_ascii=False, indent=4).encode('utf8')
print(res.decode())
