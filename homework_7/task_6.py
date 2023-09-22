# 6. Дорабатываем функции из предыдущих задач.
# Генерируйте файлы в указанную директорию — отдельный параметр функции.
# Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
import os
from task_5 import create_file_task_5


def make_directory(directory):
    if not directory in os.listdir():
        os.mkdir(directory)


def create_file_task_6(count, directory):
    make_directory(directory)
    path = directory + os.path.sep
    create_file_task_5(count=count, path=path)


if __name__ == '__main__':
    create_file_task_6(count=7, directory='task_6')
