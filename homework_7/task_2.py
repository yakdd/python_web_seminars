# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# Полученные имена сохраните в файл.
from string import ascii_lowercase as letters
import random as rnd

vowles = 'euiyoa'
name_len = range(5, 8)


def create_name(count):
    for _ in range(count):
        name_list = rnd.choices(letters, k=rnd.choice(range(2, 6)))
        add_vowles = [rnd.choice(vowles) for _ in range(2)]
        name_list.extend(add_vowles)
        rnd.shuffle(name_list)
        yield ''.join(name_list).title()


def random_names(count):
    with open('file_2', 'a', encoding='utf-8') as file:
        for new_name in create_name(count):
            file.write(f'{new_name}\n')


random_names(10)
