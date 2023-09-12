# 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


def get_dict(**kwargs) -> dict:
    temp_dict = {}
    for k, val in kwargs.items():
        if type(val) in (list, dict, set):
            val = str(val)
        temp_dict[val] = k

    return temp_dict


new_dict = get_dict(first=1,
                    second='2',
                    third=('a', 'b', 'c'),
                    fourth=0.12,
                    fifth={1: 'a', 2: 'b'},
                    sixth=[0, 8, 7],
                    seventh={'a', 'q'},
                    one_more=False)

for key, value in new_dict.items():
    print(f'{key}: {value}')
