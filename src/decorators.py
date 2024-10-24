from functools import wraps
from typing import Any


def log(filename: Any = None) -> Any:
    """Суть декоратора состоит в логировании данных ему функций.
    При указании названия файла при передаче параметра декоратора filename
    логи записываются в указанный файл(при отсутствии файла он создается)
    Если файл не указан логи выводятся в командную строку stdout"""

    def wrapper(func: Any) -> Any:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message_log = f"{func.__name__} ok.\n"
                if filename:
                    with open(filename, mode="a", encoding="UTF-8") as file:
                        file.write(f"{func.__name__} started\n")
                        file.write(f"{func.__name__} finished\n")
                        file.write(message_log)
                else:
                    print(f"{func.__name__} started")
                    print(f"{func.__name__} finished")
                    print(message_log)
            except Exception as e:
                result = f"The {func.__name__} has been stopped"
                message_log = f"{func.__name__} error: {e}, inputs: {args, kwargs}\n"
                if filename:
                    with open(filename, mode="a", encoding="UTF-8") as file:
                        file.write(result + "\n")
                        file.write(message_log + "\n")
                else:
                    print(result)
                    print(message_log)
            return result

        return inner

    return wrapper
