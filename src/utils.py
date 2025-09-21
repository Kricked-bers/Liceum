import json
import logging
from typing import Any

app_logger = logging.getLogger(__name__)
logging.basicConfig(
    filename=r"C:\Users\islam\PycharmProjects\Liceum\logs\utils.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s %(funcName)s %(levelname)s: %(message)s",
)


def searching_for_json_file(directory: str = "") -> Any:
    """Функция принимает на вход строку с полным путем до json файла
    и возвращает словарь взятый из указанного файла"""
    app_logger.info("Function started.")
    app_logger.info("Checking the input data.")
    if not isinstance(directory, str) or len(directory) == 0:
        app_logger.warning("Incorrect input data. Stop program.")
        return []
    try:
        app_logger.info("The data is correct. Continuation...")
        json_result = open(directory, encoding="UTF-8")
        json_list_result = json.load(json_result)
        app_logger.info("Function finished")
        return json_list_result
    except FileNotFoundError:
        app_logger.warning("The file you are looking for is missing. The file has been created")
        open(directory, "w+", encoding="UTF-8")
        app_logger.info("Function finished")
        return []
    except json.decoder.JSONDecodeError:
        app_logger.warning("There is an error in the file you are looking for. The program has been stopped")
        return []
