# 2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = int(input('Введите число: '))
num_init = num
num_hex = ''
letters = ['a', 'b', 'c', 'd', 'e', 'f']

while num:
    if num % 16 > 9:
        elem = letters[num % 16 % 10]
    else:
        elem = num % 16
    num_hex = str(elem) + num_hex
    num //= 16

print(f'{num_init}\u2081\u2080 = {num_hex.upper()}\u2081\u2086')
print('Проверка:', num_hex == hex(num_init)[2:])
