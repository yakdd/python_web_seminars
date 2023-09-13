# 1. Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2.
# Для проверки числа на простоту используйте правило:
# «число является простым, если делится нацело только на единицу и на себя».

def gen_prime_numbers(count):
    start = 2
    while count:
        for i in range(2, start // 2 + 1):
            if start % 2 == 0 or start % i == 0:
                break
        else:
            count -= 1
            yield start
        start += 1


num = int(input('Сколько простых чисел вывести? '))
print(*gen_prime_numbers(num))
