# 2. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

from random import randint

list_ = [randint(1, 7) for _ in range(10)]
print(list_)

list_double = list(set(i for i in list_ if list_.count(i) > 1))
print(list_double)
