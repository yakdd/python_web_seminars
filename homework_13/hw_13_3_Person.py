# В организации есть два типа людей: сотрудники и обычные люди.
# Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:
# - Фамилия (строка, не пустая)
# - Имя (строка, не пустая)
# - Отчество (строка, не пустая)
# - Возраст (целое положительное число)
# Сотрудники имеют также уникальный идентификационный номер (ID),
# который должен быть шестизначным положительным целым числом.
#
# Ваша задача:
# Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях
# (Фамилия, Имя, Отчество, Возраст).
# Класс должен проверять валидность входных данных и генерировать исключения
# InvalidNameError и InvalidAgeError, если данные неверные.
#
# Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный номер (ID).
# Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.
#
# Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.
#
# Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника
# на основе суммы цифр в его ID (по остатку от деления на 7).
#
# Создать несколько объектов класса Person и Employee с разными данными и проверить,
# что исключения работают корректно при передаче неверных данных.
from random import randint

LEN_ID = 6


class NameValidator:
    def __init__(self, param_title, param_alpha):
        self.param_title = param_title
        self.param_alpha = param_alpha

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __set__(self, instance, value):
        if not self.param_title(value) or not self.param_alpha(value):
            raise InvalidNameError('Invalid name: . Name should be a non-empty string.')
        setattr(instance, self.param_name, value)


class AgeValidator:
    def __init__(self, min_value):
        self.min_value = min_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise InvalidAgeError('not age')
        if self.min_value is not None and value <= self.min_value:
            raise InvalidAgeError(f'Invalid age: {value}. Age should be a positive integer.')
        setattr(instance, self.param_name, value)


class IdValidator:
    def __init__(self, length):
        self.length = length

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __set__(self, instance, value):
        if len(value) != self.length:
            raise InvalidIdError('invalid id')
        setattr(instance, self.param_name, value)


class Person:
    lastname = NameValidator(str.istitle, str.isalpha)
    name = NameValidator(str.istitle, str.isalpha)
    surname = NameValidator(str.istitle, str.isalpha)
    age = AgeValidator(0)

    def __init__(self, lastname: str, name: str, surname: str, age: int):
        self.lastname = lastname
        self.name = name
        self.surname = surname
        self.age = age

    @property
    def birthday(self):
        self.__dict__['_age'] += 1
        return self.__dict__['_age']

    def __str__(self):
        return f'{self.__dict__["_lastname"]} ' \
               f'{self.__dict__["_name"]} ' \
               f'{self.__dict__["_surname"]}, ' \
               f'{self.__dict__["_age"]} лет'


class Employee(Person):
    ID_LIST = []
    id_emp = IdValidator(LEN_ID)

    def __init__(self, lastname: str, name: str, surname: str, age: int, id_emp: str):
        super().__init__(lastname, name, surname, age)
        self.id_emp = id_emp
        self.level = None

    def get_level(self):
        self.level = 0
        for num in self.__dict__['_id_emp']:
            self.level += int(num)
        return self.level % 7

    def __str__(self):
        return super().__str__() + ', id: ' + str(self.__dict__['_id_emp'])


class InvalidNameError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class InvalidAgeError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class InvalidIdError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


def gen_id():
    while True:
        id_ = ''
        for _ in range(LEN_ID):
            id_ += str(randint(0, 9))
        if id_ not in Employee.ID_LIST:
            Employee.ID_LIST.append(id_)
            return id_


if __name__ == '__main__':
    man_1 = Person('Прутков', 'Козьма', 'Петрович', 10)
    print(man_1)
    print(man_1.birthday)
    print(man_1.birthday)
    print(man_1.birthday)
    print(man_1.birthday)
    print(man_1)
    emp_1 = Employee('Иванов', 'Эльдар', 'Мухтарович', 50, gen_id())
    emp_2 = Employee('Петров', 'Электрон', 'Атомович', 20, gen_id())
    print(emp_1, emp_1.get_level())
    print(emp_2, emp_2.get_level())

