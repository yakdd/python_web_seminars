# Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции.
import random as rnd

MIN_ = -1000
MAX_ = 1000


def fill_file(lines: int, name: str):
    with open(f'{name}', 'a', encoding='utf-8') as file:
        for _ in range(lines):
            file.write(f'{rnd.randint(MIN_, MAX_):>6}\t|\t{round(rnd.uniform(MIN_, MAX_), 4)}\n')


fill_file(11, 'file_1')
