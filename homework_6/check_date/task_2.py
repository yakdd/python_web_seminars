from sys import argv
from task_1 import check_date

if len(argv) != 2:
    print('Введите дату для проверки на високосность')
else:
    print(check_date(argv[1]))
