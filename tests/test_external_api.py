import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import transaction_analiz
from src.utils import searching_for_json_file

file_1 = searching_for_json_file(r"C:\Users\islam\PycharmProjects\Liceum\data\operations.json")[0]
file_2 = searching_for_json_file(r"C:\Users\islam\PycharmProjects\Liceum\data\operations.json")[1]
load_dotenv()
api_token = os.getenv("API_KEY")
headers = {"apikey": api_token}
ans_dict = {
    "success": True,
    "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
    "info": {"timestamp": 1729587482, "rate": 96.82903},
    "date": "2024-10-22",
    "result": 555.555,
}
ans_dict_json = """{"success": true,"query": {"from": "USD","to": "RUB","amount": 8221.37},"info": 
{"timestamp": 1729590002,"rate": 96.601358},"date": "2024-10-22","result": 555.555}"""
params = {
    "to": "RUB",
    "from": file_2["operationAmount"]["currency"]["code"],
    "amount": file_2["operationAmount"]["amount"],
}


@patch("requests.get")
def test_transaction_analiz_api(mock_get):
    mock_get.return_value.text = ans_dict_json
    assert transaction_analiz(file_2) == 555.555
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert", params=params, headers=headers
    )


def test_transaction_analiz_no_api():
    assert transaction_analiz(file_1) == 31957.58
