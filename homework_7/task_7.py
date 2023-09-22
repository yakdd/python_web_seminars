# 7. Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
from task_5 import dict_file_type
from task_6 import create_file_task_6, make_directory
import os


def moving_file(file, location):
    location += file
    os.rename(file, location)


def create_file_task_7(count, directory):
    create_file_task_6(count, directory)
    os.chdir(directory)

    for key in dict_file_type.keys():
        make_directory(key)

    for key, value in dict_file_type.items():
        for file in os.listdir():
            file_type = file.split('.')[-1]
            if file_type in value:
                moving_file(file, key + '/')


if __name__ == '__main__':
    create_file_task_7(count=25, directory='task_7')
