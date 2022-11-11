import requests
import json
from config import keys

class APIException(Exception):
    pass

class Converter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote.lower()]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base.lower()]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        url = f"https://api.apilayer.com/currency_data/convert?to={base_ticker}&from={quote_ticker}&amount={amount}"
        payload = {}
        headers = {
            "apikey": "TxXCXIyrEHIrmMJN07YZ35Kv0z9Jsj80"
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        dirt_result = json.dumps(response.text).split()
        result = ''
        for a in dirt_result[-1]:
            if a in '1234567890' or a == '.':
                result += a

        return result