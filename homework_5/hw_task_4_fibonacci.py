# 4. Создайте функцию генератор чисел Фибоначчи
import time


def gen_fibonacci():
    current = 0
    next = 1
    while True:
        time.sleep(0.5)
        yield current
        current, next = next, current + next


for i in gen_fibonacci():
    print(i)
