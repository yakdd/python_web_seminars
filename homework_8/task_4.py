# 4. Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.
import csv
import json


def csv_to_json(csv_file: str, json_file: str):
    with (
        open(csv_file, 'r', encoding='utf-8') as f_csv,
        open(json_file, 'w', encoding='utf-8') as f_json,
    ):
        my_dict = {}
        csv_reader = csv.reader(f_csv)
        for i, line in enumerate(csv_reader):
            if i == 0:
                continue
            line[0] = line[0].zfill(10)
            line[1] = line[1].title()
            line.append(hash(str(line[0] + line[1])))
            # print(line)
            my_dict[line[0]] = {'name': line[1], 'level': line[2], 'hash': line[3]}

        json.dump(my_dict, f_json, indent=4)


if __name__ == '__main__':
    CSV_FILE = 'task_3.csv'
    JSON_FILE = 'task_4.json'
    csv_to_json(CSV_FILE, JSON_FILE)
