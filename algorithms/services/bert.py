import pickle
from pathlib import Path

from services.constants import BERT_MODEL_FILENAME

BERT_MODEL = None


def get_bert_embedding_model():
    global BERT_MODEL
    if not BERT_MODEL:
        BERT_MODEL = load(BERT_MODEL_FILENAME)
    return BERT_MODEL


def save(embedder):
    pass


def load(file_name: str):
    file_path = Path(f"services/{file_name}")
    if file_path.is_file():
        with open(file_path, 'rb') as file:
            unpickler = pickle.Unpickler(file)
            return unpickler.load()


if __name__ == '__main__':
    print(load(BERT_MODEL_FILENAME))
