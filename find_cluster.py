from sentence_transformers import SentenceTransformer, util
from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
import pickle
from pathlib import Path
from playground import clear_df
embedder = SentenceTransformer('distilbert-base-nli-mean-tokens')




my_file = Path("./embeddings.pickle")
corpus_df = pd.read_csv('tg.csv')
clear_df(corpus_df)
corpus = corpus_df['message'].to_list()
if my_file.is_file():
    with open(my_file, 'rb') as file:
        unpickler = pickle.Unpickler(file)
        corpus_embeddings = unpickler.load()
else:
    # Corpus with example sentence
    corpus_embeddings = embedder.encode(corpus)
    # Normalize the embeddings to unit length
    corpus_embeddings = corpus_embeddings /  np.linalg.norm(corpus_embeddings, axis=1, keepdims=True)
    with open(my_file, 'wb') as file:
        corpus_embeddings = pickle.dump(corpus_embeddings, file, pickle.HIGHEST_PROTOCOL)
    



# Perform kmean clustering
clustering_model = AgglomerativeClustering(n_clusters=None, affinity='cosine', linkage='average', distance_threshold=0.1) #, affinity='cosine', linkage='average', distance_threshold=0.4)
clustering_model.fit(corpus_embeddings)
cluster_assignment = clustering_model.labels_
clustered_sentences = {}
for sentence_id, cluster_id in enumerate(cluster_assignment):
    if cluster_id not in clustered_sentences:
        clustered_sentences[cluster_id] = []

    clustered_sentences[cluster_id].append(corpus[sentence_id])

for i, cluster in clustered_sentences.items():
    print("Cluster ", i+1)
    print(cluster)
    print("")
# clusters = util.community_detection(corpus_embeddings, min_community_size=25, threshold=0.75)