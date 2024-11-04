import logging
from typing import Union

app_logger = logging.getLogger(__name__)
logging.basicConfig(
    filename=r"C:\Users\islam\PycharmProjects\Liceum\logs\masks.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s %(funcName)s %(levelname)s: %(message)s",
)


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Функция принимает на вход номер карты и возвращает
    шифрованный номер со звездами вместо некоторых цифр"""
    app_logger.info("Function started.")
    app_logger.info("Checking the input data.")
    if isinstance(card_number, (str, int)) and len(str(card_number)) > 0 and len(str(card_number)) == 16:
        app_logger.info("The data is correct. Continuation...")
        card_number = str(card_number)
        separation_card_number = [card_number[i : i + 4] for i in range(0, len(card_number), 4)]
        separation_card_number[2] = "****"
        separation_card_number[1] = separation_card_number[1][:2] + "**"
        app_logger.info("Function finished")
        return " ".join(separation_card_number)
    else:
        app_logger.warning("Incorrect input data. Stop program.")
        return "-1"


def get_mask_account(mask_account: Union[int, str]) -> Union[int, str]:
    """Функция принимает на вход номер счета и возвращает только последние четыре цифры номера
    скрывая остальные"""
    app_logger.info("Function started.")
    app_logger.info("Checking the input data.")
    if isinstance(mask_account, (str, int)) and len(str(mask_account)) > 0 and len(str(mask_account)) == 20:
        app_logger.info("The data is correct. Continuation...")
        mask_account = str(mask_account)
        app_logger.info("Function finished")
        return "**" + mask_account[-4:]
    else:
        app_logger.warning("Incorrect input data. Stop program.")
        return "-1"
