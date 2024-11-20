import csv
from typing import Any

import pandas as pd


def csv_analyzer(directory: str) -> list:
    '''Функция принимает на вход путь до csv файла и
    возращает список со словарями'''
    if not isinstance(directory, str) or len(directory) == 0:
        return []
    try:
        with open(directory, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            return list(reader)
    except FileNotFoundError:
        return []


def xls_analyzer(directory: str) -> Any:
    '''Функция принимает на вход путь до xlsx файла и
    возращает список со словарями'''
    if not isinstance(directory, str) or len(directory) == 0:
        return []
    try:
        dataframe = pd.read_excel(directory)
        dataframe = dataframe.to_dict("records")
        return dataframe
    except FileNotFoundError:
        return []

