class User:

    def __init__(self, name: str, user_id: int, level: int = 3, min_lvl=1, max_lvl=7):
        self.min_lvl = min_lvl
        self.max_lvl = max_lvl
        if not name.isalpha():
            raise ValueError('Имя должно быть текстового вида')
        self.name = name
        if not isinstance(user_id, int):
            raise ValueError('идентификатор должен быть целым числом')
        self.id = user_id
        if not isinstance(level, int) or level not in range(min_lvl, max_lvl + 1):
            raise ValueError(f'Уровень доступа должен быть целым числом от {self.min_lvl} до {self.max_lvl}')
        self.lvl = level

    def __eq__(self, other):
        return (self.name == other.name) and (self.id == other.id)

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}", {self.id}, {self.lvl})'


if __name__ == '__main__':
    user1 = User('Petr', 4, 1)
    user2 = User('Pavel', 4, 1)
    print(user1)
    print(user2)
