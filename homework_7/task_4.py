# 4. Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
# - расширение
# - минимальная длина случайно сгенерированного имени, по умолчанию 6
# - максимальная длина случайно сгенерированного имени, по умолчанию 30
# - минимальное число случайных байт, записанных в файл, по умолчанию 256
# - максимальное число случайных байт, записанных в файл, по умолчанию 4096
# - количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.
from string import digits, ascii_letters as letters
from random import choice, randbytes


def check_file_name(file_name, names):
    if file_name in names:
        return file_name + '_'
    return file_name


def create_file_task_4(ext: str, min_len=6, max_len=30, min_byte=256, max_byte=4096, count=42, path=''):
    names_list = []
    symbols = letters + digits
    for i in range(count):
        name = path + ''
        for _ in range(choice(range(min_len, max_len + 1))):
            name += choice(symbols)
        name = check_file_name(name, names_list)
        names_list.append(name)
        name += f'.{ext}'
        write_file(name, min_byte, max_byte)


def write_file(path, min_byte=256, max_byte=4096):
    with open(path, 'a') as file:
        for _ in range(choice(range(min_byte, max_byte + 1))):
            file.write(str(randbytes(1)))


if __name__ == '__main__':
    create_file_task_4('txt', min_len=2, max_len=10, min_byte=5, max_byte=10, count=3)
