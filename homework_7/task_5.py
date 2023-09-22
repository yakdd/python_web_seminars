# 5. Доработаем предыдущую задачу.
# Создайте новую функцию которая генерирует файлы с разными расширениями.
# Расширения и количество файлов функция принимает в качестве параметров.
# Количество переданных расширений может быть любым.
# Количество файлов для каждого расширения различно.
# Внутри используйте вызов функции из прошлой задачи
from task_4 import create_file_task_4
from random import choice

dict_file_type = {
    'documents': ['txt', 'doc', 'xls'],
    'applications': ['exe'],
    'audio': ['mp3', 'wav', 'ogg', 'wma'],
    'video': ['avi', 'flv', 'mov', 'mp4', 'mpeg'],
    'pictures': ['jpg', 'jpeg', 'bmp', 'png', 'gif'],
    'scripts': ['py', 'js', 'cs', 'java'],
}
other_types = ['bin', 'xml', 'apk', 'zip']
ext_list = [val for value in dict_file_type.values() for val in value]
ext_list.extend(other_types)
extensions_list = tuple(ext_list)


def create_file_task_5(count=10, path=''):
    global extensions_list
    extensions = list(extensions_list)
    while count:
        current_count = choice((range(1, count + 1)))
        count -= current_count
        ext = choice(extensions)
        create_file_task_4(ext=ext, count=current_count, path=path)
        extensions.remove(ext)


if __name__ == '__main__':
    create_file_task_5(7)
