from time import sleep

import pandas as pd
from emoji.core import replace_emoji

from algorithms.realtime_pipeline import Pipeline
from algorithms.services.constants import CHANNELS
from algorithms.services.tg_news_updater import get_tg_client


class TGPipe(Pipeline):
    def __init__(self):
        super(Pipeline).__init__()
        self.tg = get_tg_client()

    async def start(self):
        prev_list = []
        while not self.stop:
            msg_list = []
            for channel in CHANNELS:
                channel_entity = await self.tg.get_entity(channel)
                async for message in self.tg.iter_messages(channel_entity, limit=10):
                    if message.message == "" or message.message is None:
                        continue
                    text = replace_emoji(message.message)
                    msg_list.append({'message': text,
                                     'source': channel,
                                     'date': message.date.timestamp(),
                                     'views': message.views
                                     })
                    if msg_list[-1] in prev_list:
                        break
            if len(msg_list) == 0:
                continue
            prev_list = msg_list
            data = pd.DataFrame(msg_list, columns=['message', 'source', 'date', 'views'])
            self.update_res(data)
            sleep(30)
