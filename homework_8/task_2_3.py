# 2. Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.
# -------------------------------------------------------------------------------------
# 3. Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
import json
import csv
import os


def load_json():
    if os.path.exists(PATH_DB):
        with open(PATH_DB, 'r', encoding='utf-8') as file:
            data = json.load(file)
    else:
        data = {}
    return data


def input_name():
    return input('Введите имя: ')


def input_id(users_dict):
    user_id_list = []
    for value in users_dict.values():
        for key in value.keys():
            user_id_list.append(key)
    while True:
        u_id = input('Введите ID: ')
        if u_id.isdigit() and u_id not in user_id_list:
            return u_id
        print('Такой ID занят. Введите новый: ')


def input_level():
    while True:
        u_level = input('Введите уровень доступа (от 1 до 7): ')
        if u_level.isdigit() and (0 < int(u_level) < 8):
            return u_level
        print('Неверный уровень доступа. Введите новый: ')


def add_user():
    while True:
        user_name = input_name()
        if not user_name:
            break
        users_db = load_json()
        user_id = input_id(users_db)
        user_level = input_level()

        if user_level in users_db:
            for key, value in users_db.items():
                if user_level == key:
                    value[user_id] = user_name
        else:
            users_db[user_level] = {user_id: user_name}

        with (
            open(PATH_DB, 'w', encoding='utf-8') as f_json,
            open(CSV_FILE, 'w', newline='', encoding='utf-8') as f_csv
        ):
            json.dump(users_db, f_json, indent=2)
            result = []
            for level, users in users_db.items():
                for i, user in users.items():
                    result.append([i, user, level])
            csv_file = csv.writer(f_csv, dialect='excel')
            csv_file.writerow(['ID', 'Name', 'Level'])
            csv_file.writerows(result)


if __name__ == '__main__':
    PATH_DB = 'task_2.json'
    CSV_FILE = 'task_3.csv'
    add_user()
