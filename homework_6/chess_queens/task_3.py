# 3. Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
from random import randint


def random_put_queens():
    global eight_queens
    while len(eight_queens) < 8:
        while True:
            hor = randint(1, 8)
            ver = randint(1, 8)
            if (hor, ver) not in eight_queens:
                eight_queens.append((hor, ver))
                break


def get_diagonals(position: tuple) -> list:
    diagonals = []

    i = position[0]
    j = position[1]
    while i > 1 and j > 1:
        i -= 1
        j -= 1
        diagonals.append((i, j))

    i = position[0]
    j = position[1]
    while i > 1 and j < 8:
        i -= 1
        j += 1
        diagonals.append((i, j))

    i = position[0]
    j = position[1]
    while i < 8 and j < 8:
        i += 1
        j += 1
        diagonals.append((i, j))

    i = position[0]
    j = position[1]
    while i < 8 and j > 1:
        i += 1
        j -= 1
        diagonals.append((i, j))

    return diagonals


def check_diagonals(position: tuple, chess_board: list) -> bool:
    diagonals = get_diagonals(position)
    for position in diagonals:
        if position in chess_board:
            return False
    else:
        return True


def is_safety_position(chess_board):
    candidate = tuple()
    for i in range(len(chess_board)):
        for next_queen in chess_board[i + 1:]:
            # проверка горизонтали и вертикали для текущего ферзя:
            if chess_board[i][0] == next_queen[0] or chess_board[i][1] == next_queen[1]:
                return False
        else:
            candidate = chess_board[i]
    else:
        # проверка диагоналей для текущего ферзя:
        if check_diagonals(candidate, chess_board):
            return True
    return False


def print_chess_board(eight_queens):
    letters = 'ABCDEFGH'
    print(' +', '-' * 24, '+', sep='')
    for i in range(1, 9):
        print(f'{len(eight_queens) - i + 1}|', end='')
        for j in range(1, 9):
            current_cell = (i, j)
            print(' Ф ', end='') if current_cell in eight_queens else print(' . ', end='')
        print('|')
    print(' +', '-' * 24, '+\n   ', sep='', end='')
    for letter in letters:
        print(f'{letter}  ', end='')


eight_queens = []
if __name__ == '__main__':
    # eight_queens = [(3, 1), (5, 2), (2, 3), (8, 4), (6, 5), (4, 6), (7, 7), (1, 8)]  # true
    # eight_queens = [(1, 6), (3, 2), (7, 8), (3, 7), (5, 8), (3, 3), (7, 1), (8, 1)]  # false
    random_put_queens()
    print(eight_queens)
    print(f'Эта расстановка ферзей друг относительно друга безопасная?: {is_safety_position(eight_queens)}')
    print_chess_board(eight_queens)
