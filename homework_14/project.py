import json
from user import User
from my_exception import AccessError


class Project:
    USERS = []
    USER_LEVEL = None

    def __init__(self):
        pass

    @classmethod
    def load_data(cls, path):
        """ Загружаем пользователей из json-файла в список класса USERS"""
        try:
            with open(path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    for id_, name in value.items():
                        cls.USERS.append(User(name, int(id_), int(key)))
            return cls.USERS
        except FileNotFoundError as e:
            print(f'Text error: {e}')
            print(f'База данных пуста. Добавляю пользователя Admin, id: 0, права доступа: 1')

    @classmethod
    def show_users(cls):
        """ Вывод пользователей в консоль """
        item, name_head, id_head, level_head = '#', 'name', 'ID', 'level'
        max_name_len = max([len(user.name) for user in cls.USERS]) + 1
        max_id_len = max([len(str(user.id)) for user in cls.USERS]) + 1
        table_hr = f'+---+{"-" * max_name_len}+{"-" * max_id_len}+--------+'
        print(table_hr)
        print(f'{item:^5}{name_head:<{max_name_len}} {id_head:^{max_id_len}} {level_head:^{len(level_head) + 2}}')
        print(table_hr)
        for i, user in enumerate(cls.USERS):
            print(
                f'{i + 1:>3}. {user.name:<{max_name_len}} {user.id:>{max_id_len}} {user.lvl:^{len(level_head) + 2}}'
            )
        print(table_hr)

    @classmethod
    def login(cls):
        """ Авторизация """
        name, user_id = input('Sign up: для авторизации введите имя и id пользователя через пробел: ').split()
        try:
            user_id = int(user_id)
        except TypeError as e:
            print(e)
        else:
            name = name.title()
            # Создаем временного пользователя и проверяем есть ли такой в базе:
            temp_user = User(name, user_id)
            for user in cls.USERS:
                if temp_user == user:
                    temp_user = user
                    cls.USER_LEVEL = temp_user.lvl
                    print(f'{temp_user.name}, Вы автоизованы. Ваш уровень доступа: {temp_user.lvl}')
                    return cls.USER_LEVEL
            else:
                del temp_user
                raise AccessError('Пользователь не найден.')

    @classmethod
    def add_user(cls):
        """ Добавляем нового пользователя """
        if not cls.USER_LEVEL and cls.USER_LEVEL != 0:
            cls.login()
        while True:
            try:
                name = input('Введите имя: ').title()
                the_id = int(input('Введите личный идентификатор: '))
                level = int(input('Введите уровень доступа: '))

                # Создаем нового пользователя с правами доступа ниже, чем у залогиненного пользователя:
                new_user = User(name, the_id, level, min_lvl=cls.USER_LEVEL + 1)
                for user in cls.USERS:
                    if new_user.id == user.id:
                        print('Такой ID уже занят. Попробуйте еще раз.')
                        del new_user
                        break
                else:
                    cls.USERS.append(new_user)  # добавляем нового пользователя с список класса
                    cls.rewrite_db()  # перезаписываем json-файл
                    return new_user
            except ValueError as e:
                print(e)

    @classmethod
    def rewrite_db(cls):
        data = {}
        for user in cls.USERS:
            data.setdefault(user.lvl, {user.id: user.name})
            data[user.lvl].update({user.id: user.name})
        with open(PATH, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)

    @classmethod
    def root_user(cls):
        """ Создаем первого пользователя, если база пуста """
        cls.USERS.append(User('Admin', 0, level=1))
        cls.USER_LEVEL = 0


PATH = 'user_db.json'
if __name__ == '__main__':
    init_data = Project.load_data(PATH)
    if init_data:
        print(Project.USERS)
    else:
        Project.root_user()
        print(Project.USERS)
