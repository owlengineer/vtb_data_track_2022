from telethon import TelegramClient
from services.constants import CHANNELS


api_id = ''                                                                                         # From https://my.telegram.org/
api_hash = ''
TG_CLIENT = TelegramClient('session', api_id, api_hash)
TG_CLIENT.start()



