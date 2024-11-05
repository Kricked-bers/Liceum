from unittest.mock import Mock, patch

import pytest

from src.file_analyzer import csv_analyzer, xls_analyzer


@pytest.fixture
def exit_answer():
    return [
        {
            "id": 650703,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 3598919,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 593027,
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "amount": 30368,
            "currency_name": "Shilling",
            "currency_code": "TZS",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 366176,
            "state": "EXECUTED",
            "date": "2020-08-02T09:35:18Z",
            "amount": 29482,
            "currency_name": "Rupiah",
            "currency_code": "IDR",
            "from": "Discover 0325955596714937",
            "to": "Visa 3820488829287420",
            "description": "Перевод с карты на карту",
        },
    ]


directory = r"C:\Users\islam\PycharmProjects\Liceum\data\test_excel.xlsx"


@patch("csv.DictReader")
def test_csv_analyzer_basic(mock, exit_answer):
    mock.return_value = exit_answer
    assert csv_analyzer(directory) == exit_answer


def test_csv_analyzer_empty():
    assert csv_analyzer("") == []
    assert csv_analyzer(566) == []
    assert csv_analyzer(r"C:\Users\islam\PycharmProjects\Liceum\data\none.xlsx") == []


@patch("pandas.read_excel")
def test_xls_analyzer_basic(mock_read_excel, exit_answer):
    mock_dataframe = Mock()
    mock_dataframe.to_dict.return_value = exit_answer
    mock_read_excel.return_value = mock_dataframe
    assert xls_analyzer(directory) == exit_answer


def test_xls_analyzer_empty():
    assert xls_analyzer("") == []
    assert xls_analyzer(566) == []
    assert xls_analyzer(r"C:\Users\islam\PycharmProjects\Liceum\data\none.xlsx") == []
