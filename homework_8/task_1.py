# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки.
import json


def txt_to_json(file, name_json):
    my_dict = {}
    with (open(file, 'r', encoding='utf-8') as f_read,
          open(name_json, 'w', encoding='utf-8') as f_write):
        for line in f_read:
            tmp = line.strip().split(' | ')
            my_dict[tmp[0].title()] = float(tmp[1])
        json.dump(my_dict, f_write, indent=2)
    # print(my_dict)


if __name__ == '__main__':
    txt_to_json('file_3.txt', 'task_1.json')
