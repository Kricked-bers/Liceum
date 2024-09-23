from datetime import datetime
from typing import Union

from src.widget import get_date


def filter_by_state(dictionary: list, state_input: str = "EXECUTED") -> Union[list, str]:
    exit_lists = list()
    for element_lists in dictionary:
        if element_lists["state"] == state_input:
            exit_lists.append(element_lists)
    return exit_lists


def sort_by_date(dictionary: list) -> list:
    dates_nosort = [get_date(element["date"]) for element in dictionary]
    dates_format_datetime = [datetime.strptime(date, "%Y-%m-%d") for date in dates_nosort]
    dates_format_datetime.sort(reverse=True)
    dates_format_normal = [runcode_date.strftime("%Y-%m-%d") for runcode_date in dates_format_datetime]
    dictionary_dates_sort = list()
    for normal_date in dates_format_normal:
        for dictionary_element in dictionary:
            element_get_date = get_date(dictionary_element["date"])
            if element_get_date == normal_date:
                dictionary_dates_sort.append(dictionary_element)
    return dictionary_dates_sort
