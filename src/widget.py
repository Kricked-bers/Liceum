from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_number_card: str) -> str:
    """Функция принимает на вход номер карты или счета
    и возвращает зашифрованный номер карты или счета с указанием"""
    for element in account_number_card.split():
        try:
            int(element)
            if len(element) == 16:
                return f"{" ".join(account_number_card.split()[:-1])} {get_mask_card_number(element)}"
            elif len(element) == 20:
                return f"{" ".join(account_number_card.split()[:-1])} {get_mask_account(element)}"
        except ValueError:
            continue
    return "-1"


def get_date(date_format: str) -> str:
    """Функция принимает на вход дату в определенном формате
    и возвращает в формате ДД.ММ.ГГГ"""
    formated_date = date_format[:10].split("-")
    formated_date[0], formated_date[2] = formated_date[2], formated_date[0]
    return ".".join(formated_date)

