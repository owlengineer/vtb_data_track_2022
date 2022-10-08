from sentence_transformers import SentenceTransformer, util
from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
import pickle
from rutermextract import TermExtractor
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
clustering_model = AgglomerativeClustering(n_clusters=None, distance_threshold=0.4)
clustering_model.fit(corpus_embeddings)
cluster_assignment = clustering_model.labels_
clustered_sentences = {}
for sentence_id, cluster_id in enumerate(cluster_assignment):
    if cluster_id not in clustered_sentences:
        clustered_sentences[cluster_id] = []

    clustered_sentences[cluster_id].append(corpus[sentence_id])

result_clusters = {}
term_extractor = TermExtractor()
for i, cluster in clustered_sentences.items():
    keywords = []
    for keyword in term_extractor(''.join(cluster)):
        if keyword.count < 3:
            continue
        keywords.append((keyword.normalized, keyword.count))
    if len(keywords) != 0:
        result_clusters[i] = {"keywords": keywords, "texts": cluster}

print(result_clusters)
# clusters = util.community_detection(corpus_embeddings, min_community_size=25, threshold=0.75)