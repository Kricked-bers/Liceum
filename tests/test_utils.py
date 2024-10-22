from src.utils import searching_for_json_file

search_test_file = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
]
search_real_file = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560",
}


def test_searching_for_json_file_basic():
    assert searching_for_json_file(r"C:\Users\islam\PycharmProjects\Liceum\data\test.json") == search_test_file
    assert (
        searching_for_json_file(r"C:\Users\islam\PycharmProjects\Liceum\data\operations.json")[1] == search_real_file
    )


def test_searching_for_json_file_empty_and_none_file():
    assert searching_for_json_file(r"C:\Users\islam\PycharmProjects\Liceum\data\none.json") == []
    assert searching_for_json_file() == []
    assert searching_for_json_file(50) == []
