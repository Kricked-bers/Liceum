import json
import os

import requests
from dotenv import load_dotenv


def transaction_analiz(transaction: dict) -> float:
    '''Функуия принимает на вход транзакцию в виде словаря и возвращает сумму транзакции в рублях,
    если транзакция была произведена в другой валюте функция обращается к внешнему API и производит конвертацию'''
    load_dotenv()
    api_token = os.getenv("API_KEY")
    headers = {"apikey": api_token}
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    else:
        params = {
            "to": "RUB",
            "from": transaction["operationAmount"]["currency"]["code"],
            "amount": transaction["operationAmount"]["amount"],
        }
        url = "https://api.apilayer.com/exchangerates_data/convert"
        response = requests.get(url, params=params, headers=headers)
        amount_from_rub = json.loads(response.text)
        return float(amount_from_rub["result"])
