import csv
import re
from collections import Counter
from typing import Any

import pandas as pd


def csv_analyzer(directory: str) -> list:
    """Функция принимает на вход путь до csv файла и
    возращает список со словарями"""
    if not isinstance(directory, str) or len(directory) == 0:
        return []
    try:
        with open(directory, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            return list(reader)
    except FileNotFoundError:
        return []


def xls_analyzer(directory: str) -> Any:
    """Функция принимает на вход путь до xlsx файла и
    возращает список со словарями"""
    if not isinstance(directory, str) or len(directory) == 0:
        return []
    try:
        dataframe = pd.read_excel(directory)
        dataframe = dataframe.to_dict("records")
        return dataframe
    except FileNotFoundError:
        return []


def re_search_string(transactions: list, search_string: str) -> list:
    """Функция принимает на вход список словарей и строку
    и возвращает список словарей в описании которых есть искомое слово"""
    if (
        not isinstance(transactions, list)
        or not isinstance(search_string, str)
        or len(transactions) == 0
        or len(search_string) == 0
    ):
        return []
    new_list_transactions = []
    for transaction in transactions:
        if re.search(search_string, transaction["description"], flags=re.IGNORECASE):
            new_list_transactions.append(transaction)
    return new_list_transactions


def counting_in_the_dictionary(transactions: list, search_desk: list) -> list:
    """Функция принимает на вход список словарей и список описаний транзакий
    и возвращает словарь типа Описание: Кол-во записей с списке словарей с искомым описанием"""
    if (
        not isinstance(transactions, list)
        or not isinstance(search_desk, list)
        or len(transactions) == 0
        or len(search_desk) == 0
    ):
        return []
    list_descriptions = [i["description"] for i in transactions]
    ans_list = []
    count_list = Counter(list_descriptions)
    for i in count_list.keys():
        if i.lower() in [j.lower() for j in search_desk]:
            ans_list.append({i: count_list[i]})
    return ans_list
