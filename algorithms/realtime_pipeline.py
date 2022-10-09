from hashlib import new
from time import sleep
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from services.constants import CHANNELS
from services.bert import get_bert_embedding_model
from services.clusterization import fit_cluster, create_map_of_cluster, get_keywords_from_cluster
from utils.processing import get_data, clear_df
from emoji.core import replace_emoji
from services.tg_news_updater import TG_CLIENT

class Pipeline:
    def __init__(self):
        self.df = get_data()
        self.encoder = SentenceTransformer('distilbert-base-nli-mean-tokens')
        self.stop = False
        self.raw_msgs = self.df.message.to_list()
        self.embedded_data = get_bert_embedding_model()

        self.labels = fit_cluster(self.embedded_data)
        clustered_sentences = create_map_of_cluster(self.labels, self.raw_msgs)
        self.result_clusters = get_keywords_from_cluster(clustered_sentences)
        print("Init done")

    def update_res(self, df):
        clear_df(df)
        self.df += df
        new_data = df["message"].to_list()
        # Corpus new data
        corpus_embeddings = self.encoder.encode(new_data)
        # Normalize the embeddings to unit length for new data
        corpus_embeddings = corpus_embeddings / np.linalg.norm(corpus_embeddings, axis=1, keepdims=True)
        # Update embedded
        self.embedded_data = np.concatenate((self.embedded_data, corpus_embeddings))
        # Update raw msgs
        self.raw_msgs += new_data
        # Update labels
        self.labels = fit_cluster(self.embedded_data)
        # Update resulting clusters
        clustered_sentences = create_map_of_cluster(self.labels, self.raw_msgs)
        self.result_clusters = get_keywords_from_cluster(clustered_sentences)

    def stop(self):
        self.stop = True

    async def start(self):
        prev_list = []
        while not self.stop:
            msg_list = []
            for channel in CHANNELS:
                channel_entity= await TG_CLIENT.get_entity(channel)
                async for message in TG_CLIENT.iter_messages(channel_entity, limit=10):
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



if __name__=='__main__':
    pipeline = Pipeline()
    TG_CLIENT.loop.run_until_complete(pipeline.start())
