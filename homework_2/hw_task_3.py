# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

import fractions


def short_fraction(num: int, denum: int) -> str:
    ''' Сокращение дроби '''
    x = num
    y = denum
    while y:
        x, y = y, x % y

    short_fraction_str = '/'.join([str(int(num / x)), str(int(denum / x))])
    return short_fraction_str


fraction_1 = input('Введите первую дробь: ')
fraction_2 = input('Введите вторую дробь: ')

numerator_1 = int(fraction_1.split('/')[0])
denumerator_1 = int(fraction_1.split('/')[1])
numerator_2 = int(fraction_2.split('/')[0])
denumerator_2 = int(fraction_2.split('/')[1])

comm_denumerator = denumerator_1 * denumerator_2
summ_numerator = numerator_1 * denumerator_2 + numerator_2 * denumerator_1
mult_numerator = numerator_1 * numerator_2

if summ_numerator == comm_denumerator:
    summ = '1'
    mult = '/'.join([str(mult_numerator), str(comm_denumerator)])
elif mult_numerator == comm_denumerator:
    summ = '/'.join([str(summ_numerator), str(comm_denumerator)])
    mult = '1'
else:
    summ = '/'.join([str(summ_numerator), str(comm_denumerator)])
    mult = '/'.join([str(mult_numerator), str(comm_denumerator)])


print('===============================')
print(f'Сумма дробей = {summ} = {short_fraction(summ_numerator, comm_denumerator)}')
print(f'Произведение дробей = {mult} = {short_fraction(mult_numerator, comm_denumerator)}')

print('Проверка:')
f_one_init = fractions.Fraction(numerator_1, denumerator_1)
f_two_init = fractions.Fraction(numerator_2, denumerator_2)

print(f'{f_one_init} + {f_two_init} = {f_one_init + f_two_init}')
print(f'{f_one_init} * {f_two_init} = {f_one_init * f_two_init}')
