# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.
import os
import json
import csv
import pickle


def create_json(content: dict, name: str):
    with open(name, 'w', encoding='utf-8') as file:
        json.dump(content, file, indent=4)


def create_csv(content: dict, name: str):
    with open(name, 'w', newline='', encoding='utf-8') as f_csv:
        lines = []
        for key, value in list(content.items()):
            line = [key]
            for val in value:
                line.append(val)
            lines.append(line)

        csv_writer = csv.writer(f_csv, dialect='excel')
        csv_writer.writerow(['path', 'it is', 'size (byte)', 'parent'])
        csv_writer.writerows(lines)


def create_pickle(content: dict, name: str):
    with open(name, 'wb') as file:
        pickle.dump(content, file, protocol=pickle.DEFAULT_PROTOCOL)


def count_size_directory(catalog: str):
    total_size = 0
    for element in os.listdir(catalog):
        path_element = os.path.join(catalog, element)
        if os.path.isfile(path_element):
            total_size += os.path.getsize(path_element)
        elif os.path.isdir(path_element):
            total_size += count_size_directory(path_element)
    return total_size


def inspect_folder(catalog: str = os.getcwd()):
    global FOLDER_CONTENT

    for element in os.listdir(catalog):
        if not element.startswith('.'):  # пропускаем git-элементы
            path_element = os.path.join(catalog, element)
            FOLDER_CONTENT[path_element] = []
            if os.path.isfile(path_element):
                FOLDER_CONTENT[path_element].append('is_file')
                FOLDER_CONTENT[path_element].append(os.path.getsize(path_element))
            elif os.path.isdir(path_element):
                FOLDER_CONTENT[path_element].append('is_directory')
                FOLDER_CONTENT[path_element].append(count_size_directory(path_element))
                FOLDER_CONTENT[path_element].append(os.path.abspath(os.path.join(path_element, os.pardir)))

                inspect_folder(path_element)

    return FOLDER_CONTENT


FOLDER_CONTENT = {}
if __name__ == '__main__':
    inspect_folder(os.path.abspath(os.path.join('..')))
    create_json(FOLDER_CONTENT, 'folder_content.json')
    create_csv(FOLDER_CONTENT, 'folder_content.csv')
    create_pickle(FOLDER_CONTENT, 'folder_content.pickle')
