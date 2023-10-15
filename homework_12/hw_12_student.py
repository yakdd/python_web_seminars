# Задание: Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
import csv


class Validator:
    def __init__(self, param_title, param_alpha):
        self.param_title = param_title
        self.param_alpha = param_alpha

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __set__(self, instance, value):
        if self.param_title(value) and self.param_alpha(value):
            setattr(instance, self.param_name, value)
        else:
            raise ValueError(f'Bad {value}')


class Student:
    lastname = Validator(str.istitle, str.isalpha)
    name = Validator(str.istitle, str.isalpha)
    surname = Validator(str.istitle, str.isalpha)

    def __init__(self, lastname: str, name: str, surname: str):
        self.lastname = lastname
        self.name = name
        self.surname = surname
        self.subjects = self.get_subjects()

    def get_subjects(self):
        with open('subjects.csv', 'r', newline='', encoding='utf-8') as file:
            csv_file = csv.reader(file)
            subjects_list = [{subj: {'grades': [], 'tests': []}} for line in csv_file for subj in line]
        return subjects_list

    def add_grade(self, subject: str, grade: int):
        if not (1 < grade < 6):
            raise ValueError(f'Оценка {grade} должна быть от 2 до 5 баллов')
        for subj_dict in self.subjects:
            for key, value in subj_dict.items():
                if key == subject:
                    value['grades'].append(grade)
                    break

    def add_test_score(self, subject: str, grade: int):
        if not (0 <= grade < 101):
            raise ValueError(f'Результат теста {grade} должн быть от 0 до 100 баллов')
        for subj_dict in self.subjects:
            for key, value in subj_dict.items():
                if key == subject:
                    value['tests'].append(grade)
                    break

    def get_average_grade(self):
        all_grades = []
        for subj_dict in self.subjects:
            for value in subj_dict.values():
                for k, val in value.items():
                    if k == 'grades':
                        all_grades.extend(val)
        return sum(all_grades) / len(all_grades)

    def get_average_test_score(self, subject):
        for subj_dict in self.subjects:
            for key, value in subj_dict.items():
                if key == subject:
                    return sum(value['tests']) / len(value['tests'])

    def __str__(self):
        return f'{self.__dict__["_lastname"]} {self.__dict__["_name"]} {self.__dict__["_surname"]}'

    def __repr__(self):
        return f'{self.__class__.__name__}(' \
               f'"{self.__dict__["_lastname"]}",' \
               f'"{self.__dict__["_name"]}",' \
               f'"{self.__dict__["_surname"]}")'


first = 'Иванов Кузьма Михалыч'
studer_1 = Student(*first.split())
print(studer_1)
print(repr(studer_1))
print(studer_1.subjects)
print()
studer_1.add_grade('Математика', 4)
studer_1.add_grade('Математика', 3)
studer_1.add_grade('Физика', 5)
studer_1.add_test_score("Математика", 85)
studer_1.add_test_score("Математика", 17)
studer_1.add_test_score("История", 92)
studer_1.add_test_score("Физика", 40)
print(studer_1.subjects)
print()
current_subj = "Математика"
print(f'Успеваемость студента (средний балл) {studer_1}: {studer_1.get_average_grade()}')
print(f'Средний результат по тестам по предмету {current_subj}: {studer_1.get_average_test_score(current_subj)}')
