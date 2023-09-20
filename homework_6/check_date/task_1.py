# 1. Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.
_months = {1: 31, 2: 29, 3: 31,
           4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30,
           10: 31, 11: 30, 12: 31}


def _check_february(year: int) -> bool:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False


def check_date(date: str) -> bool:
    global _months
    day, month, year = map(int, date.split('.'))
    if day > _months[month] or day < 1:
        return False
    if month < 1 or month > 12:
        return False
    if year < 1 or year > 9999:
        return False
    else:
        if month == 2 and day == 29:
            if not _check_february(year):
                return False
    return True


if __name__ == '__main__':
    new_date = '29.02.2020'
    print(check_date(new_date))
