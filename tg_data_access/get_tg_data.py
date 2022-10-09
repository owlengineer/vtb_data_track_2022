import csv
import pandas as pd
from telethon.client import TelegramClient
from datetime import datetime
from telethon.tl.types import InputMessagesFilterPhotos
from emoji.core import replace_emoji


def remove_emoji(text):
    return replace_emoji(text)


# URLs or tg names
channels = ["https://t.me/consultant_plus", "https://t.me/MinEconomyrf", "https://t.me/cbrrf",
            "https://t.me/eglavbukru",
            "https://t.me/MoscowExchangeOfficial", "https://t.me/garantnews", "https://t.me/klerkonline",
            "https://t.me/nalog_gov_ru",
            "https://t.me/mintsifry", "https://t.me/SberInvestments", "https://t.me/minfin",
            "https://t.me/centralbank_russia",
            "https://t.me/investfuture", "https://t.me/markettwits"]
api_id = ''  # From https://my.telegram.org/
api_hash = ''

all_messages = {}


async def main():
    data = pd.DataFrame(columns=["message", "source", "date", "views"])
    msg_list = []
    for channel in channels:
        channel_entity = await client.get_entity(channel)
        all_messages[channel] = []
        async for message in client.iter_messages(channel_entity, filter=InputMessagesFilterPhotos):
            if message.message == "":
                continue
            if message.date.timestamp() < datetime(year=2019, month=1, day=1).timestamp():
                break
            text = remove_emoji(message.message)
            msg_list.append({'message': text,
                             'source': channel,
                             'date': message.date.timestamp(),
                             'views': message.views
                             })
        print(f"{channel=} ended")
    data = pd.DataFrame(msg_list, columns=['message', 'source', 'date', 'views'])
    data.to_csv("tg_news.csv")


if __name__ == "__main__":
    client = TelegramClient('test_session', api_id, api_hash)
    client.start()
    with client:
        client.loop.run_until_complete(main())
