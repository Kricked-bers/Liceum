from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_number_card: str) -> str:
    """Функция принимает на вход номер карты или счета
    и возвращает зашифрованный номер карты или номер счета с указанием типа"""
    if not isinstance(account_number_card, str) or len(account_number_card) == 0:
        return "-1"
    for element in account_number_card.split():
        try:
            int(element)
            if len(element) == 16:
                element_answer = account_number_card.split()[:-1]
                return (
                    f"{(" ".join(element_answer)) + " " if len(element_answer) > 0 else ""}"
                    f"{get_mask_card_number(element)}"
                )
            elif len(element) == 20:
                return f"{" ".join(account_number_card.split()[:-1])} {get_mask_account(element)}"
        except ValueError:
            continue
    return "-1"


def get_date(date: str, date_format: str = "Y-m-d") -> str:
    """Функция принимает на вход дату в определенном формате
    и возвращает в формате ГГГГ-ММ-ДД"""
    if not isinstance(date, str) or len(date) == 0:
        return "-1"
    if date_format == "d-m-Y":
        formated_date = date[:10].split("-")
        formated_date[0], formated_date[2] = formated_date[2], formated_date[0]
        return "-".join(formated_date)
    elif date_format == "d.m.Y":
        formated_date = date[:10].split("-")
        formated_date[0], formated_date[2] = formated_date[2], formated_date[0]
        return ".".join(formated_date)
    else:
        return date[:10]
