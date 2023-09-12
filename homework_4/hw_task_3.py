# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
#
# Задание №6
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

def show_balance():
    global balance
    print(f'Текущий баланс = {balance}')


def add_percent(percent=0.03):
    """ Начисление 3% за каждую трерью операцию на счете """
    global balance
    if len(history) % 3 == 0:
        balance += balance * percent
        history.append(balance * percent)


def count_tax_sum(take_summ, min_=30, max_=600) -> int | float:
    """ Вычисление суммы процентов за снятие денег """
    global tax
    tax_sum = take_summ * tax
    if tax_sum < min_:
        tax_sum = min_
    elif tax_sum > max_:
        tax_sum = max_

    return tax_sum


def check_balance(plus=0, minus=0) -> bool:
    """ Проверка баланса перед операцией """
    global balance, multiplicator
    if plus and plus % multiplicator == 0:
        return True
    if minus and minus % multiplicator == 0:
        if minus + count_tax_sum(minus) <= balance:
            return True
    return False


def check_wealth(percent=0.1):
    """ Проверка на "богатство" """
    global balance
    if balance > 5 * 10 ** 6:
        balance -= balance * percent
        history.append(-balance * percent)


def add_money():
    """ Операция добавления денег на счет """
    global balance, multiplicator
    show_balance()
    plus = int(input(f'Внесите деньги (сумма должна быть кратна {multiplicator}): '))
    if check_balance(plus):
        balance += plus
        history.append(plus)
        add_percent()
        check_wealth()
        show_balance()
    else:
        print('Ошибочно указана сумма.')


def take_money():
    """ Операция снятия денег со счета """
    global balance, multiplicator
    show_balance()
    if balance:
        minus = int(input(f'Сумма снятия (сумма должна быть кратна {multiplicator}): '))
        if check_balance(minus):
            balance -= (minus + count_tax_sum(minus))
            history.append(-minus)
            history.append(-count_tax_sum(minus))
            add_percent()
            show_balance()
        else:
            print('Ошибочно указана сумма.')
    else:
        print('Недостаточно средств на счете.')


def start():
    actions = ['выйти', 'пополнить счет', 'снять наличные']
    while True:
        print('------------------')
        print('Выберете действие: ')
        for i, action in enumerate(actions):
            print(f'\t{i} - {action}')

        choice = input('>>> ')
        if choice.isdigit() and (int(choice) <= len(actions) - 1):  # ????????????????????????????????????????????
            match choice:
                case '1':
                    add_money()
                case '2':
                    take_money()
                case '0':
                    break
        else:
            print('Ошибка ввода. Попробуйте еще раз!')


multiplicator = 50
tax = 0.015
balance = 0
history = []
start()
print(history)
