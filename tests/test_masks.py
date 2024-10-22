import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "input, exit",
    [("12548569562145875236", "**5236"), ("65895452658452456985", "**6985"), ("56895625458565856556", "**6556")],
)
def test_get_mask_account_basic(input, exit):
    assert get_mask_account(input) == exit


def test_get_mask_account_empty():
    assert get_mask_account("") == "-1"


def test_get_mask_account_type():
    assert get_mask_account(("element_1", "element_2")) == "-1"
    assert get_mask_account([1, 3, 5]) == "-1"


@pytest.mark.parametrize(
    "input_1, exit_1",
    [
        ("7854695815624587", "7854 69** **** 4587"),
        ("1254869562154658", "1254 86** **** 4658"),
        ("4587698514523654", "4587 69** **** 3654"),
    ],
)
def test_get_mask_card_number_basic(input_1, exit_1):
    assert get_mask_card_number(input_1) == exit_1


def test_get_mask_card_number_empty():
    assert get_mask_card_number("") == "-1"


def test_get_mask_card_number_type():
    assert get_mask_card_number(("element", 15)) == "-1"
    assert get_mask_card_number([45, 58, "element"]) == "-1"
