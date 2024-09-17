from typing import Union


def mask_account_card(account_number_card: Union[str]) -> Union[str]:
    """Функция принимает на вход номер карты или счета
    и возвращает зашифрованный номер карты или счета с указанием"""
    for element in account_number_card.split():
        try:
            int(element)
            if len(element) == 16:
                separation_card_number = [element[i : i + 4] for i in range(0, len(element), 4)]
                separation_card_number[2] = "****"
                separation_card_number[1] = separation_card_number[1][:2] + "**"
                return (
                    f"{" ".join(account_number_card.split()[:account_number_card.split().index(element)])} "
                    f"{" ".join(separation_card_number)}"
                )
            elif len(element) == 20:
                return account_number_card.split()[0] + " **" + element[-4:]
        except ValueError:
            return "-1"


def get_date(date_format: Union[str]) -> str:
    """Функция принимает на вход дату в определенном формате
    и возвращает в формате ДД.ММ.ГГГ"""
    formated_date = date_format[:10].split("-")
    formated_date[0], formated_date[2] = formated_date[2], formated_date[0]
    return ".".join(formated_date)
