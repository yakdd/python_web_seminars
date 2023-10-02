# Напишите следующие функции:
# - Нахождение корней квадратного уравнения
# - Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# - Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# - Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import csv
import json
from random import randint
from typing import Callable
from functools import wraps

file_name = input('Введите имя файла для сохранения данных: ')


def search_roots_from_csv(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        equations_roots = []
        with open(f'{file_name}.csv', 'r', newline='', encoding='utf-8') as file:
            csv_file = csv.reader(file)
            for line in csv_file:
                a, b, c = list(map(int, line))
                result = list(func(a, b, c))
                equations_roots.append(set(result))

        return equations_roots

    return wrapper


def json_decorator(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        equation_dict = {}
        with (
            open(f'{file_name}.csv', 'r', newline='', encoding='utf-8') as f_csv,
            open(f'{file_name}.json', 'w', encoding='utf-8') as f_json,
        ):
            csv_file = csv.reader(f_csv)
            for i, line in enumerate(csv_file):
                equation_dict[str(result[i])] = line

            json.dump(equation_dict, f_json, indent=4)

        return result

    return wrapper


@json_decorator
@search_roots_from_csv
def quadratic_equation(a: int, b: int, c: int) -> set:
    x_1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    x_2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    return {x_1, x_2}


def get_coefficients_csv(left: int = -100, right: int = 100) -> list:
    data = []
    for _ in range(randint(100, 1000)):
        # исключаем ноль для коэффициента "а":
        while True:
            three_coefficients = [randint(left, right) for _ in range(3)]
            if three_coefficients[0] != 0:
                break
        data.append(three_coefficients)
    with open(f'{file_name}.csv', 'w', newline='', encoding='utf-8') as file:
        csv_file = csv.writer(file, dialect='excel')
        csv_file.writerows(data)

    return data


if __name__ == '__main__':
    print(get_coefficients_csv())
    print(quadratic_equation())
