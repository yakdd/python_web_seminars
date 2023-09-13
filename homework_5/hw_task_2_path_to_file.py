# 2. Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def path_to_file(string):
    *path, file = string.split('\\')
    path = '\\'.join([*path])
    # С двойным обратным слэшем заколебался! Так и не понял, как поменять его на одиночный.
    file, ext = file.split('.')
    return path, file, ext


link = 'D:\PYTHON\math_informik\prime numbers.jpg'
print(path_to_file(link))
