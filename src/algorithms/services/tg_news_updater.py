from telethon import TelegramClient
from algorithms.services.constants import CHANNELS

TG_CLIENT = None
api_id = ''  # From https://my.telegram.org/
api_hash = ''


def get_tg_client():
    global TG_CLIENT
    if not TG_CLIENT:
        TG_CLIENT = TelegramClient('session', api_id, api_hash)
        TG_CLIENT.start()
    return TG_CLIENT
