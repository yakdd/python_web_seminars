# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# - имя файла без расширения или название каталога,
# - расширение, если это файл,
# - флаг каталога,
# - название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование
import os
import logging
from collections import namedtuple

SLASH = os.path.sep
OBJECTS_LIST = []
Object = namedtuple('Object', ['object_name', 'extention', 'is_dir', 'parent_dir'], defaults=[False, False, False])

format_log = '{levelname:<5}- Function:{funcName}():\t{msg}'
logging.basicConfig(filename='homework_15.log', filemode='w', encoding='utf-8',
                    format=format_log, style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_path_file(path_to_parse: str):
    *_, full_name = path_to_parse.split(SLASH)
    name, ext = full_name.rsplit('.', 1)
    new_object = Object(name, ext)
    logger.info(f'Name:{name}, extention:{ext}')
    return new_object


def parse_path_dir(path_to_parse: str):
    *_, parent_dir, current_dir = path_to_parse.rsplit(SLASH, 2)
    new_object = Object(current_dir, is_dir=True, parent_dir=parent_dir)
    logger.info(f'Name:{current_dir}, is directory, parent directory:{parent_dir}')
    return new_object


def inspect_folder(catalog: str):
    for element in os.listdir(catalog):
        if not element.startswith('.'):
            path_element = os.path.join(catalog, element)
            if os.path.isfile(path_element):
                OBJECTS_LIST.append(parse_path_file(path_element))
            elif os.path.isdir(path_element):
                OBJECTS_LIST.append(parse_path_dir(path_element))
                inspect_folder(path_element)
    return OBJECTS_LIST


path = os.path.abspath(os.path.join('..'))

if __name__ == '__main__':
    print(path)
    directory_content = inspect_folder(path)
    for i, item in enumerate(directory_content):
        print(f'{i + 1}. {item}')
