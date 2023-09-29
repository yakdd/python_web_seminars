# 5. Напишите функцию, которая ищет json файлы в указанной директории
# и сохраняет их содержимое в виде одноимённых pickle файлов.
import json
import os
import pickle


def json_to_pickle(task_path: str = os.getcwd()):
    for path, folders, files in os.walk(task_path):
        for file in files:
            if file.endswith('.json'):
                name = file.rsplit('.', maxsplit=1)[0]
                with (
                    open(f'{name}.json', 'r', encoding='utf-8') as f_json,
                    open(f'{name}.pickle', 'wb') as f_pickle,
                ):
                    json_reader = json.load(f_json)
                    pickle.dump(json_reader, f_pickle)


if __name__ == '__main__':
    json_to_pickle()
