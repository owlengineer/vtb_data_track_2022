from hashlib import new
from time import sleep
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from algorithms.services.constants import CHANNELS
from algorithms.services.bert import get_bert_embedding_model
from algorithms.services.clusterization import fit_cluster, create_map_of_cluster, get_keywords_from_cluster
from algorithms.utils.processing import get_data, clear_df
from emoji.core import replace_emoji


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
        self.process()

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
        self.process()

    def process(self):
        pass

    def get_digest(self, role):
        return [""]

    def get_trends(self):
        return

    def get_insights(self):
        return []

    def stop(self):
        self.stop = True

    async def start(self):
        pass


if __name__ == '__main__':
    pipeline = Pipeline()
    TG_CLIENT.loop.run_until_complete(pipeline.start())
