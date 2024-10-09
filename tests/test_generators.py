import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def input_dict():
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
    return transactions


@pytest.fixture
def input_dict_no_usd():
    transactions = [
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
    return transactions


exit_dict_filter_by_currency_usd_next_1 = {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702",
}
exit_dict_filter_by_currency_usd_next_2 = {
    "id": 142264268,
    "state": "EXECUTED",
    "date": "2019-04-04T23:20:05.206878",
    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод со счета на счет",
    "from": "Счет 19708645243227258542",
    "to": "Счет 75651667383060284188",
}
exit_dict_filter_by_currency_usd_next_3 = {
    "id": 895315941,
    "state": "EXECUTED",
    "date": "2018-08-19T04:27:37.904916",
    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод с карты на карту",
    "from": "Visa Classic 6831982476737658",
    "to": "Visa Platinum 8990922113665229",
}
exit_dict_filter_by_currency_rub_next_1 = {
    "id": 873106923,
    "state": "EXECUTED",
    "date": "2019-03-23T01:09:46.296404",
    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
    "description": "Перевод со счета на счет",
    "from": "Счет 44812258784861134719",
    "to": "Счет 74489636417521191160",
}
exit_dict_filter_by_currency_rub_next_2 = {
    "id": 594226727,
    "state": "CANCELED",
    "date": "2018-09-12T21:27:25.241689",
    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
    "description": "Перевод организации",
    "from": "Visa Platinum 1246377376343588",
    "to": "Счет 14211924144426031657",
}
exit_dict_transaction_descriptions_input_dict = [
    "Перевод организации",
    "Перевод со счета на счет",
    "Перевод со счета на счет",
    "Перевод с карты на карту",
    "Перевод организации",
]
exit_dict_transaction_descriptions_input_dict_no_usd = ["Перевод со счета на счет", "Перевод организации"]


def test_filter_by_currency_basic_usd(input_dict):
    generator_usd = filter_by_currency(input_dict, "USD")
    assert next(generator_usd) == exit_dict_filter_by_currency_usd_next_1
    assert next(generator_usd) == exit_dict_filter_by_currency_usd_next_2
    assert next(generator_usd) == exit_dict_filter_by_currency_usd_next_3
    with pytest.raises(StopIteration):
        next(generator_usd)


def test_filter_by_currency_basic_rub(input_dict):
    generator_rub = filter_by_currency(input_dict, "RUB")
    assert next(generator_rub) == exit_dict_filter_by_currency_rub_next_1
    assert next(generator_rub) == exit_dict_filter_by_currency_rub_next_2
    with pytest.raises(StopIteration):
        next(generator_rub)


def test_filter_by_currency_empty_no_currency(input_dict_no_usd):
    assert next(filter_by_currency("")) == "-1"
    generator_no_usd = filter_by_currency(input_dict_no_usd, "USD")
    with pytest.raises(StopIteration):
        next(generator_no_usd)


def test_filter_by_currency_type():
    assert next(filter_by_currency(125, "")) == "-1"
    assert next(filter_by_currency(dict({"a": "b"}), "")) == "-1"


def test_transaction_descriptions_basic(input_dict, input_dict_no_usd):
    assert list(transaction_descriptions(input_dict)) == exit_dict_transaction_descriptions_input_dict
    assert list(transaction_descriptions(input_dict_no_usd)) == exit_dict_transaction_descriptions_input_dict_no_usd


def test_transaction_descriptions_empty():
    assert next(transaction_descriptions("")) == "-1"


def test_transaction_descriptions_type():
    assert next(transaction_descriptions(152)) == "-1"


def test_card_number_generator_basic():
    test_card_generator = card_number_generator(1, 5)
    assert next(test_card_generator) == "0000 0000 0000 0001"
    assert next(test_card_generator) == "0000 0000 0000 0002"
    assert next(test_card_generator) == "0000 0000 0000 0003"
    assert next(test_card_generator) == "0000 0000 0000 0004"
    assert next(test_card_generator) == "0000 0000 0000 0005"


def test_card_number_generator_empty_type():
    assert next(card_number_generator(1, "")) == "-1"
    assert next(card_number_generator("", 5)) == "-1"
    assert next(card_number_generator(-1, 5)) == "-1"
    assert next(card_number_generator(99999999999999999, 5)) == "-1"
    assert next(card_number_generator(1, 99999999999999999999)) == "-1"
    with pytest.raises(StopIteration):
        next(card_number_generator(9, 5))
