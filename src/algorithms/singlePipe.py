from algorithms.realtime_pipeline import Pipeline
from algorithms.tgpipe import TGPipe

PIPELINE = None


def get_pipeline(is_tg=False):
    global PIPELINE
    if not PIPELINE:
        PIPELINE = (TGPipe if is_tg else Pipeline)()
    return PIPELINE


if __name__ == '__main__':
    print(type(get_pipeline()))
