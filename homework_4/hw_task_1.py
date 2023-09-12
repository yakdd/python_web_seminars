# 1. Напишите функцию для транспонирования матрицы
from random import randint


def create_random_matrix(min_=2, max_=5):
    rows = randint(min_, max_)
    cols = randint(min_, max_)
    matrix = [[randint(0, 9) for _ in range(cols)] for _ in range(rows)]
    return matrix


def matrix_transposition(matrix: list[list]) -> list[list]:
    # создаем нулевую матрицу, обратную исходной:
    matrix_t = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]

    # транспонируем в нулевую матрицу исходную:
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix_t[j][i] = matrix[i][j]

    return matrix_t


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print()


matrix_init = create_random_matrix()
print('Исходная матрица:')
print_matrix(matrix_init)

matrix_transpos = matrix_transposition(matrix_init)
print('Транспонированая матрица:')
print_matrix(matrix_transpos)
