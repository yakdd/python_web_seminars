# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# - Какие вещи взяли все три друга
# - Какие вещи уникальны, есть только у одного друга
# - Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
friends = {
    'Андрей': ('палатка', 'спальник', 'посуда', 'одежда', 'нож', 'фонарь', 'аптечка'),
    'Антон': ('котелок', 'спальник', 'посуда', 'одежда', 'нож', 'фонарь', 'аптечка'),
    'Олег': ('топор', 'спальник', 'посуда', 'одежда', 'нож', 'фонарь'),
}
# {'нож', 'топор', 'аптечка', 'посуда', 'спальник', 'фонарь', 'палатка', 'одежда', 'котелок'}


print('1. Какие вещи взяли все три друга:')
all_things = set()
for k, v in friends.items():
    new_things = set(v)
    all_things = all_things.union(new_things)
print('Все вещи: ', all_things)

everybody_things = all_things
for k, v in friends.items():
    new_things = set(v)
    everybody_things = everybody_things.intersection(new_things)
print('Вещи, которые есть у каждого: ', everybody_things)


print('2. Уникальные вещи, есть только у одного друга:', end=' ')
unique_things_step_1 = set()
for k, v in friends.items():
    new_things = set(v)
    elements = all_things.difference(new_things)
    unique_things_step_1 = unique_things_step_1.union(elements)

unique_things_step_2 = set()
for k, v in friends.items():
    elements = set(v).intersection(unique_things_step_1)
    unique_things_step_2 = unique_things_step_2.symmetric_difference(elements)
print(unique_things_step_2)


print('3. Вещи, которые есть у всех друзей кроме одного и его имя:', end=' ')
new_set = unique_things_step_1.difference(unique_things_step_2)
name = ''
for element in new_set:
    for friend, things in friends.items():
        if element not in things:
            name = friend
print(f'У всех друзей кроме {name} есть {new_set}')
