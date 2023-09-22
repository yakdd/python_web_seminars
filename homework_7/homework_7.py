# Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов.
#     При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла.
#     Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени.
#     Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
#     К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
import os
from task_5 import create_file_task_5
from task_6 import make_directory


def group_renaming(digits: int, init_ext, new_ext, span: list, new_name=''):
    """
    :param digits:      количество цифр в порядковом номере
    :param init_ext:    расширение исходного файла
    :param new_ext:     расширение конечного файла
    :param span:        диапазон сохраняемого оригинального имени
    :param new_name:    желаемое конечное имя файла
    :return:
    """
    for i, item in enumerate(os.listdir(), start=1):
        if item.endswith(init_ext):
            # формируем порядковый номер:
            serial_number = ''
            for _ in range(digits - len(str(i))):
                serial_number += '0'
            serial_number += str(i)

            # формируем новое имя файла:
            only_name = '.'.join(item.split('.')[:-1])
            result = only_name[span[0] - 1:span[1]] + '_' + new_name + '_' + serial_number + '.' + new_ext

            os.rename(item, result)


if __name__ == '__main__':
    directory = 'homework_7'
    make_directory(directory)
    os.chdir(directory)
    create_file_task_5(50)
    group_renaming(3, 'mp4', 'xxx', [3, 7], 'homework')
