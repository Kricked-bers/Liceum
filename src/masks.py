from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Функция принимает на вход номер карты и возвращает
    шифрованный номер со звездами вместо некоторых цифр"""
    if isinstance(card_number, (str, int)) and len(str(card_number)) > 0:
        card_number = str(card_number)
        separation_card_number = [card_number[i : i + 4] for i in range(0, len(card_number), 4)]
        separation_card_number[2] = "****"
        separation_card_number[1] = separation_card_number[1][:2] + "**"
        return " ".join(separation_card_number)
    else:
        return "-1"


def get_mask_account(mask_account: Union[int, str]) -> Union[int, str]:
    """Функция принимает на вход номер счета и возвращает только последние четыре цифры номера
    скрывая остальные"""
    if isinstance(mask_account, (str, int)) and len(str(mask_account)) > 0:
        mask_account = str(mask_account)
        return "**" + mask_account[-4:]
    else:
        return "-1"
