from src.widget import get_date, mask_account_card


def test_mask_account_card_basic():
    assert mask_account_card("Maestro 5569458756985215") == "Maestro 5569 45** **** 5215"
    assert mask_account_card("Счет 54569856985214584568") == "Счет **4568"
    assert mask_account_card("Visa Gold 4584565425145687") == "Visa Gold 4584 56** **** 5687"
    assert mask_account_card("2545562654526589") == "2545 56** **** 6589"


def test_mask_account_card_empty():
    assert mask_account_card("") == "-1"


def test_mask_account_card_type():
    assert mask_account_card(("Maestro", 54))
    assert mask_account_card(["Visa", 4524])


def test_get_date_basic():
    assert get_date("2019-05-15F12:25:23") == "2019-05-15"
    assert get_date("2024-10-25F12:25:23") == "2024-10-25"
    assert get_date("2005-12-05F12:25:23") == "2005-12-05"


def test_get_date_basic_state():
    assert get_date("2019-05-15F12:25:23", "d-m-Y") == "15-05-2019"
    assert get_date("2024-10-25F12:25:23", "d-m-Y") == "25-10-2024"
    assert get_date("2005-12-05F12:25:23", "d-m-Y") == "05-12-2005"


def test_get_date_empty():
    assert get_date("") == "-1"


def test_get_date_type():
    assert get_date(("25-05-2019", 15), "") == "-1"
    assert get_date(["date", 25 - 10 - 2003], "") == "-1"
