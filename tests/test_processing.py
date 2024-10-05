from src.processing import filter_by_state, sort_by_date

input_dict = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
exit_dict_filter_by_state_executed = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]
exit_dict_filter_by_state_canceled = [
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
exit_dict_sort_by_date_true = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]
exit_dict_sort_by_date_false = [
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
]


def test_filter_by_state_basic_state():
    assert filter_by_state(input_dict, "EXECUTED") == exit_dict_filter_by_state_executed
    assert filter_by_state(input_dict, "CANCELED") == exit_dict_filter_by_state_canceled


def test_filter_by_state_empty():
    assert filter_by_state("") == "-1"


def test_filter_by_state_type():
    assert filter_by_state((1, 5, "dict")) == "-1"
    assert filter_by_state("Nodict") == "-1"
    assert filter_by_state(52445) == "-1"


def test_filter_by_state_type_state():
    assert filter_by_state(input_dict, 52154) == "-1"
    assert filter_by_state(input_dict, ("NotStr", "15")) == "-1"


def test_sort_by_date_basic_default():
    assert sort_by_date(input_dict) == exit_dict_sort_by_date_true


def test_sort_by_date_empty():
    assert sort_by_date([]) == "-1"


def test_sort_by_date_type():
    assert sort_by_date(4521) == "-1"
    assert sort_by_date(input_dict, False) == "-1"
    assert sort_by_date({1: 2, 2: 2}, "False") == "-1"


def test_sort_by_date_filter():
    assert sort_by_date(input_dict, "True") == exit_dict_sort_by_date_true
    assert sort_by_date(input_dict, "False") == exit_dict_sort_by_date_false
