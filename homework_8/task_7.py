# 7. Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Распечатайте его как pickle-строку
import csv
import pickle


def csv_to_pickle_string(csv_file: str):
    my_dict = {}
    with open(csv_file, 'r', newline='', encoding='utf-8') as f_csv:
        csv_reader = csv.reader(f_csv)

        keys = []
        table = []
        # заполняем пустой словарь 'my_dict' ключами (первая строка 'csv_reader'):
        for i, line in enumerate(csv_reader):
            if i == 0:
                for item in line:
                    my_dict[item] = []
                    keys.append(item)
            else:
                table.append(line)

        # присваиваем ключам словаря 'my_dict' значения соответсвующих столбцов 'csv_reader':
        table = list(zip(*table))
        for i, key in enumerate(keys):
            my_dict[key] = table[i]

        # print(my_dict)
        result = pickle.dumps(my_dict, protocol=pickle.DEFAULT_PROTOCOL)
        return result


if __name__ == '__main__':
    CSV_FILE = 'task_6.csv'
    print(csv_to_pickle_string(CSV_FILE))
