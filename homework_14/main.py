from project import Project, PATH


def main():
    start.login()
    while True:
        print('Выберете действие:')
        action = int(input('  1: показать всех пользователей\n'
                           '  2: добавить пользователя\n'
                           '  0: выйти из программы\n'
                           '>>> '))
        if action == 0:
            return
        elif action == 1:
            start.show_users()
        elif action == 2:
            start.add_user()
        else:
            print('Ошибка ввода. Попробуйте еще раз.')


if __name__ == '__main__':
    start = Project()
    data = start.load_data(PATH)  # считываем базу данных
    if data:
        main()
    else:
        Project.root_user()  # создаем root-пользователя
        print(Project.USERS)
        main()
