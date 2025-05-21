# integration/quote_api_adapter.py

import requests
import urllib3
from domain.factories import Factory

# Отключаем предупреждение о небезопасном соединении (InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class QuoteApiAdapter:
    def __init__(self, api_url="https://api.quotable.io/quotes/random"):
        self.api_url = api_url

    def fetch_quote(self):
        response = requests.get(self.api_url, verify=False)
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list):
                if len(data) > 0:
                    data = data[0]
                else:
                    raise Exception("Получен пустой список цитат")
            try:
                quote = Factory.create_quote(data["content"], data["author"])
                return quote
            except KeyError as e:
                raise Exception(f"Неверная структура ответа API, отсутствует ключ: {e}")
        else:
            raise Exception(f"Ошибка при получении цитаты: {response.status_code}")
