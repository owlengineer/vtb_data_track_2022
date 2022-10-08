from sentence_transformers import SentenceTransformer
from sklearn.cluster import AgglomerativeClustering
import numpy as np

embedder = SentenceTransformer('distilbert-base-nli-mean-tokens')

# Corpus with example sentences
corpus = ['Утвердили график переноса выходных в 2023 году\n\nПраздничные дни 1 и 8 января совпали с выходными. Их '
          'перенесли на 24 февраля и 8 мая. С учетом этого отдохнем:\n31 декабря – 8 января;\n23–26 февраля;\n8 '
          'марта;\n29 апреля – 1 мая;\n6-9 мая;\n10-12 июня;\n4-6 ноября.\n\nДокументы:\nИнформация с сайта '
          'Правительства РФ от 30.08.2022 \nПостановление Правительства РФ от 29.08.2022 № 1505\n\nПосмотреть '
          'информацию о количестве рабочих и выходных дней в 2023 году всегда можно в системе КонсультантПлюс в '
          'Производственном календаре для пятидневной и шестидневной рабочей недели.\nВ календаре также приводятся '
          'нормы рабочего времени в часах для разных режимов работы.\n\nПолучить бесплатный пробный доступ к '
          'КонсультантПлюс https://login.consultant.ru/demo-access/',
          'Ключевую ставку продолжают снижать\n\nС 25 июля ключевая ставка равна 8%, что на 1,5 процентных пункта '
          'ниже предыдущего значения. Такое решение Банк России принял на очередном заседании.\n\nВновь обратиться к '
          'этому вопросу ЦБ РФ планирует 16 сентября.\n\nИнформация Банка России от 22.07.2022\n\nПолучить бесплатный '
          'пробный доступ к КонсультантПлюс https://login.consultant.ru/demo-access/',
          'Попробуйте свои силы в рубрике «Вопрос на засыпку».\nВыберите один из предложенных вариантов. Ответ и '
          'обоснование опубликуем в понедельник.',
          'Попробуйте свои силы в рубрике «Вопрос на засыпку».\nВыберите один из предложенных вариантов. Ответ и '
          'обоснование опубликуем в понедельник. '
          ]
corpus_embeddings = embedder.encode(corpus)

# Normalize the embeddings to unit length
corpus_embeddings = corpus_embeddings /  np.linalg.norm(corpus_embeddings, axis=1, keepdims=True)

# Perform kmean clustering
clustering_model = AgglomerativeClustering(n_clusters=None, distance_threshold=1.5) #, affinity='cosine', linkage='average', distance_threshold=0.4)
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