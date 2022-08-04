import requests
import json
from config import keys

class ConvertionException(Exception):
    pass
class CryptoConvector:
    @staticmethod
    def convert(queue: str, base: str, amout: str):
        if queue == base:
            raise ConvertionException(f'Нельзя перевести одинаковые валюты {base}')
        try:
            queue_ticker = keys[queue]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {queue}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')
        try:
            amout = float(amout)
        except KeyError:
            raise ConvertionException(f'Не удалось обработать количество {amout}')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={queue_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        return total_base
