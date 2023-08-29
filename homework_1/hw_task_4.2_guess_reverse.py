# 4.2. Загадывается случайное число от 0 до 1000.
# Написать прогрмму, которая за 10 попыток угадает это число.
from random import randint

left = 0
right = 1000

number = randint(left, right)

for i in range(10):
    _try = (left + right) // 2
    print(f'{i+1} попытка: {_try}')

    if number < _try:
        right = _try
    elif number > _try:
        left = _try
    else:
        print(f'Угадал: {_try}')
        break
else:
    print('Попытки закончились.')

print(f'Загаданное число: {number}')
