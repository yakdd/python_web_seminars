# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
#     from random import
#     randint num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT, UPPER_LIMIT, TRY = 0, 1000, 10
print(f'Угадайте число от {LOWER_LIMIT} до {UPPER_LIMIT} с {TRY} попыток')

num = randint(LOWER_LIMIT, UPPER_LIMIT)

for i in range(TRY):
    n = int(input(f'{i+1} попытка: '))
    if n < num:
        print('Загаданное число больше')
    elif n > num:
        print('Загаданное число меньше')
    else:
        print(f'Точно! {num}')
