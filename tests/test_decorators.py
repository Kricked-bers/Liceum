from src.decorators import decorator_log


def test_decorator_log_basic():
    @decorator_log()
    def calculate(x, y):
        """Функция умножающая два числа"""
        result = x * y
        return result

    test_result = calculate(2, 5)
    test_result_error = calculate(2)
    assert test_result == 10
    assert test_result_error == "The calculate has been stopped"
    assert calculate.__doc__ == "Функция умножающая два числа"


def test_decorator_log_commandline_no_error(capsys):
    @decorator_log()
    def calculate(x, y):
        """Функция умножающая два числа"""
        result = x * y
        return result

    calculate(2, 8)
    captured = capsys.readouterr()
    assert captured.out.split("\n")[0] == "calculate started"
    assert captured.out.split("\n")[1] == "calculate finished"
    assert captured.out.split("\n")[2] == "calculate ok."


def test_decorator_log_commandline_error(capsys):
    @decorator_log()
    def calculate(x, y):
        """Функция умножающая два числа"""
        result = x * y
        return result

    calculate(1)
    captured = capsys.readouterr()
    assert captured.out.split("\n")[0] == "The calculate has been stopped"
    assert (
        captured.out.split("\n")[1] == "calculate error: test_decorator_log_commandline_error.<locals>.calculate() "
        "missing 1 required positional argument: 'y', inputs: ((1,), {})"
    )


def test_decorator_log_file():
    @decorator_log(filename="log_text.txt")
    def calculate(x, y):
        result = x * y
        return result

    test_result = calculate(8, 5)
    test_result_error = calculate(2)
    assert test_result == 40
    assert test_result_error == "The calculate has been stopped"
