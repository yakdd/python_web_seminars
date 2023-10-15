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
            raise ValueError(f'ФИО должно состоять только из букв и начинаться с заглавной буквы')


class Student:
    name = Validator(str.istitle, str.isalpha)
    lastname = Validator(str.istitle, str.isalpha)

    def __init__(self, name: str, subjects_file):
        self.name, self.lastname = name.split()
        self.subjects_list = self.get_subjects(subjects_file)
        self.subject_results = {}

    def get_subjects(self, subjects_file):
        with open(subjects_file, 'r', newline='', encoding='utf-8') as file:
            csv_file = csv.reader(file)
            subjects_list = [subj for line in csv_file for subj in line]
        return subjects_list

    def add_grade(self, subject: str, grade: int):
        if not (1 < grade < 6):
            raise ValueError(f'Оценка должна быть целым числом от 2 до 5')
        if subject not in self.subjects_list:
            raise ValueError(f'Передмета {subject} нет в учебной программе')
        self.subject_results.setdefault(subject, {'grades': [], 'tests': []})
        self.subject_results[subject]['grades'].append(grade)

    def add_test_score(self, subject: str, grade: int):
        if not (0 <= grade < 101):
            raise ValueError(f'Результат теста {grade} должн быть от 0 до 100 баллов')
        if subject not in self.subjects_list:
            raise ValueError(f'Передмета {subject} нет в учебной программе')

        self.subject_results.setdefault(subject, {'grades': [], 'tests': []})
        self.subject_results[subject]['tests'].append(grade)

    def get_average_grade(self):
        all_grades = []
        for subj, results in self.subject_results.items():
            for key, value in results.items():
                if key == 'grades':
                    all_grades.extend(value)
        return sum(all_grades) / len(all_grades)

    def get_average_test_score(self, subject):
        for subj, results in self.subject_results.items():
            if subj == subject:
                return sum(results['tests']) / len(results['tests'])

    def __str__(self):
        discipline = ', '.join([key for key in self.subject_results.keys()])
        return f'Студент: {self.__dict__["_name"]} {self.__dict__["_lastname"]}\nПредметы: {discipline}'

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.__dict__["_name"]} {self.__dict__["_lastname"]}")'


# student = Student("Иван Иванов", "subjects.csv")
# print(student)
# print(repr(student))
# print()
#
# student.add_grade("Математика", 4)
# student.add_test_score("Математика", 85)
# student.add_grade("История", 5)
# student.add_test_score("История", 92)
#
# average_grade = student.get_average_grade()
# print(f"Средний балл: {average_grade}")
# average_test_score = student.get_average_test_score("Математика")
# print(f"Средний результат по тестам по математике: {average_test_score}")
# print(student)

# test_2 ============================
# student = Student("123 Иван", "subjects.csv")
# test_3 ============================
# student = Student("Петров Петр", "subjects.csv")
# student.add_grade("Физика", 6)
# test_4 ============================
student = Student("Сидоров Сидор", "subjects.csv")
average_history_score = student.get_average_test_score("Биология")

