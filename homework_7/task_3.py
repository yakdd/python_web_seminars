# 3. Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# - если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# - если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# При достижении конца более короткого файла, возвращайтесь в его начало.

def mult(name: str, nums: str) -> tuple:
    num_1, num_2 = nums.split('|')
    multiplication = round(int(num_1.strip()) * float(num_2.strip()), 4)
    if multiplication < 0:
        output = (name.lower(), str(abs(multiplication)))
    else:
        output = (name.upper(), str(round(multiplication)))
    return output


def func():
    with (
        open('file_1', 'r', encoding='utf-8') as digits,
        open('file_2', 'r', encoding='utf-8') as strings,
        open('file_3', 'w', encoding='utf-8') as file,
    ):
        new_len = max(len(list(digits)), len(list(strings)))
        strings.seek(0)
        digits.seek(0)
        for _ in range(new_len):
            name = strings.readline().strip()
            nums = digits.readline().strip()
            if not name:
                strings.seek(0)
                name = strings.readline().strip()
            if not nums:
                digits.seek(0)
                nums = digits.readline().strip()
            output = mult(name, nums)
            file.write(' | '.join(output) + '\n')


func()
