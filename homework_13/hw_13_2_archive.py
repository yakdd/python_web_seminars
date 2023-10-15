# Допишите в вашу задачу Archive обработку исключений.
# Добавьте исключение в ваш код InvalidTextError, которые будет вызываться,
# когда текст не является строкой или является пустой строкой.
# И InvalidNumberError, которое будет вызываться, если число не является
# положительным целым числом или числом с плавающей запятой.
from typing import Union


class Archive:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        if not isinstance(text, str) or len(text) == 0:
            raise InvalidTextError('Invalid text: . Text should be a non-empty string.')
        if not isinstance(number, (int, float)) or number <= 0:
            raise InvalidNumberError(f'Invalid number: {number}. Number should be a positive integer or float.')

        self.text = text
        self.number = number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'


class InvalidTextError(Exception):
    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return f'{self.msg}'


class InvalidNumberError(Exception):
    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return f'{self.msg}'


if __name__ == '__main__':
    # 1 ----------------
    # archive_instance = Archive("Sample text", 42.5)
    # print(archive_instance)

    # 2 ----------------
    # invalid_archive_instance = Archive("", -5)
    # print(invalid_archive_instance)
    # __main__.InvalidTextError: Invalid text: . Text should be a non-empty string.

    # 3 ----------------
    invalid_archive_instance = Archive("Sample text", -5)
    print(invalid_archive_instance)
    # __main__.InvalidNumberError: Invalid number: -5. Number should be a positive integer or float.
