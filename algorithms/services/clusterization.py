from typing import List

import numpy as np
from rutermextract import TermExtractor
from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA


def fit_cluster(data_after_embedding: np.ndarray,
                clustering_model=AgglomerativeClustering, n_cluster=None, distance: int = .4):
    model = clustering_model(n_clusters=n_cluster, distance_threshold=distance)
    model.fit(data_after_embedding)
    return model.labels_


def create_map_of_cluster(cluster_assignment, data_sentences: List[str]):
    clustered_sentences = {}
    for sentence_id, cluster_id in enumerate(cluster_assignment):
        if cluster_id not in clustered_sentences:
            clustered_sentences[cluster_id] = []

        clustered_sentences[cluster_id].append(data_sentences[sentence_id])
    return clustered_sentences


def get_keywords_from_cluster(clustered_sentences):
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
    return result_clusters

