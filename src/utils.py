import json
from typing import Any


def searching_for_json_file(directory: str = "") -> Any:
    '''Функция принимает на вход строку с полным путем до json файла
    и возвращает словарь взятый из указанного файла'''
    if not isinstance(directory, str) or len(directory) == 0:
        return []
    try:
        json_result = open(directory, encoding="UTF-8")
        json_list_result = json.load(json_result)
        return json_list_result
    except FileNotFoundError:
        open(directory, "w+", encoding="UTF-8")
        return []
    except json.decoder.JSONDecodeError:
        return []
