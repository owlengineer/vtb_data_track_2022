from services.bert import get_bert_embedding_model
from services.clusterization import fit_cluster, create_map_of_cluster, get_keywords_from_cluster
from utils.processing import get_data

df = get_data()
raw_msgs, raw_dates = df.message.to_list(), df.date.to_list()

embedded_data = get_bert_embedding_model()

labels = fit_cluster(embedded_data)

clustered_sentences = create_map_of_cluster(labels, {"texts": raw_msgs, "dates": raw_dates})

result_clusters = get_keywords_from_cluster(clustered_sentences)

print(result_clusters)