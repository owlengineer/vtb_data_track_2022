from typing import List

import numpy as np
from rutermextract import TermExtractor
from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
from pprint import pprint


def fit_cluster(data_after_embedding: np.ndarray,
                clustering_model=AgglomerativeClustering, n_cluster=None, distance: int = .4):
    model = clustering_model(n_clusters=n_cluster, distance_threshold=distance)
    model.fit(data_after_embedding)
    return model.labels_


def create_map_of_cluster(cluster_assignment, data):
    clustered_sentences = {}
    for sentence_id, cluster_id in enumerate(cluster_assignment):
        if cluster_id not in clustered_sentences:
            clustered_sentences[cluster_id] = []
    #    pprint(data[0][sentence_id])
    #    pprint(data[1][sentence_id])
        clustered_sentences[cluster_id].append({"text": data["texts"][sentence_id],
                                                "date": data["dates"][sentence_id]})
    return clustered_sentences


def get_keywords_from_cluster(clustered_sentences):
    result_clusters = {}
    term_extractor = TermExtractor()
    for i, cluster in clustered_sentences.items():
        keywords = []
        #pprint(cluster)
        cluster_texts = []
        for text in cluster:
            cluster_texts.append(text["text"])
        for keyword in term_extractor(''.join(cluster_texts)):
            if keyword.count < 3:
                continue
            keywords.append((keyword.normalized, keyword.count))
        if len(keywords) != 0:
            result_clusters[i] = {"keywords": keywords, "texts": cluster}
            # pprint(result_clusters[i])
    return result_clusters

