# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

baggage = {
    'sleeping_bag': 3,
    'tent': 5,
    'bowler_hat': 0.7,
    'dishes': 0.5,
    'knife': 0.2,
    'flashlight': 0.4,
    'cloth': 2,
    'axe': 1.5,
    'pharmacy': 0.7
}
# print(baggage)

backpack = 10
things = []

for k, v in baggage.items():
    if backpack >= v:
        things.append(k)
        backpack -= v
    else:
        break

    # print(k, round(backpack, 2), end=':\t')
    # print(things)

print(things)
