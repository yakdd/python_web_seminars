# 6 Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестирования возьмите pickle версию файла из задачи 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
import pickle
import csv


def pickle_to_csv(pickle_file: str, csv_file: str):
    with (

        open(pickle_file, 'rb') as f_pickle,
        open(csv_file, 'w', newline='', encoding='utf-8') as f_csv,
    ):
        my_dict = pickle.load(f_pickle)
        headers = []
        names = []
        levels = []
        hashes = []
        for user_id, user_info in my_dict.items():
            headers.append(user_id)
            names.append(user_info['name'])
            levels.append(user_info['level'])
            hashes.append(user_info['hash'])

        csv_file_writer = csv.writer(f_csv, dialect='excel')
        csv_file_writer.writerow(headers)
        csv_file_writer.writerows([names, levels, hashes])


if __name__ == '__main__':
    PICKLE_FILE = 'task_4.pickle'
    # pickle-версия файла из задачи 4: 'task_4.pickle' (получен из файла 'task_4.json')
    CSV_FILE = 'task_6.csv'
    pickle_to_csv(PICKLE_FILE, CSV_FILE)
