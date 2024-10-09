from typing import Any


def filter_by_currency(dictionary: list, currency: str = "") -> Any:
    """Функция принимает на вход список словарей и валюту и
    возвращает по очередности словари с указанным типом валюты"""
    if (
        not isinstance(dictionary, list)
        or not isinstance(currency, str)
        or (len(dictionary) == 0 or len(currency) == 0)
    ):
        yield "-1"
        return
    filter_gen = (element for element in dictionary if element["operationAmount"]["currency"]["code"] == currency)
    for filter_gen_iter in filter_gen:
        yield filter_gen_iter


def transaction_descriptions(dictionary: list) -> Any:
    """Функция принимает на вход список словарей и
    возвращает по очередности тип перевода"""
    if not isinstance(dictionary, list) or len(dictionary) == 0:
        yield "-1"
        return
    description_gen = (element["description"] for element in dictionary)
    for description_gen_iter in description_gen:
        yield description_gen_iter


def card_number_generator(begin: int, end: int) -> Any:
    """Функция принимает на вход начальное и конечное значение генерации номеров карт
    и возвращает генератор номеров карт в указанном диапазоне"""
    if (
        not isinstance(begin, int)
        or not isinstance(end, int)
        or begin < 1
        or end < 1
        or begin > 9999999999999999
        or end > 9999999999999999
        or len(str(begin)) == 0
        or len(str(end)) == 0
    ):
        yield "-1"
        return
    f = begin - 1
    for i in range(begin, end + 1):
        f += 1
        ans = "0" * (16 - len(str(f))) + str(f)
        yield " ".join([ans[i : i + 4] for i in range(0, len(ans), 4)])
