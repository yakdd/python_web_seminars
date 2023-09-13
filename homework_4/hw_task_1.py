# 1. Напишите функцию для транспонирования матрицы
from random import randint


def create_random_matrix(min_=2, max_=5):
    rows = randint(min_, max_)
    cols = randint(min_, max_)
    matrix = [[randint(0, 9) for _ in range(cols)] for _ in range(rows)]
    return matrix


# VAR_1 ====================================================
def matrix_transposition(matrix: list[list]) -> list[list]:
    # создаем нулевую матрицу, обратную исходной:
    matrix_t = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]

    # транспонируем в нулевую матрицу исходную:
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix_t[j][i] = matrix[i][j]

    return matrix_t


# VAR_2 ====================================================
def trans_for(matrix):
    temp = []
    for i in range(len(matrix[0])):
        temp.append([])
        for j in range(len(matrix)):
            temp[i].append(matrix[j][i])
    return temp


# VAR_3 ====================================================
def trans_zip(matrix):
    return list(zip(*matrix))


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print()


print('Исходная матрица:')
matrix_init = create_random_matrix()
print_matrix(matrix_init)

print('Транспонированая матрица:')
matrix_transpos = matrix_transposition(matrix_init)
print_matrix(matrix_transpos)
print('---------------------')
trans_for = trans_for(matrix_init)
print_matrix(trans_for)
print('---------------------')
trans_zip = trans_zip(matrix_init)
print_matrix(trans_zip)
