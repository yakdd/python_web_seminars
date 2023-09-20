# 4. Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.
import random
from task_3 import is_safety_position, print_chess_board


def first_queen():
    global chess_board
    global verticals

    ver = random.choice(verticals)
    chess_board.append((1, ver))
    verticals.remove(ver)
    put_eight_queens(2)


def put_eight_queens(row):
    global chess_board
    global verticals

    # следующие ферзи:
    for hor in range(row, 9):
        ver = random.choice(verticals)
        position = (hor, ver)
        if is_safety_position(chess_board):
            chess_board.append(position)
            verticals.remove(ver)
        else:
            chess_board.pop()
            verticals.append(ver)
            put_eight_queens(hor)


chess_board = []
verticals = [1, 2, 3, 4, 5, 6, 7, 8]

first_queen()
print_chess_board(chess_board)
print('\nКоличество выставленных ферзей:', len(chess_board))
