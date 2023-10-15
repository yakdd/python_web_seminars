from random import randint


class Matrix:
    """ Класс Матрица """

    def __init__(self, x: int, y: int, matrix_list=None):
        self.x = x
        self.y = y
        if not matrix_list:
            self.matrix = [[randint(0, 9) for _ in range(self.y)] for _ in range(self.x)]
        else:
            self.matrix = matrix_list

    def __repr__(self) -> str:
        return f'Matrix({self.x}, {self.y})'

    def __eq__(self, other) -> bool:
        """ Метод Сравнение матриц """
        if isinstance(self, Matrix) and isinstance(other, Matrix):
            if self.x == other.x and self.y == other.y:
                return all([self.matrix[i][j] == other.matrix[i][j] for i in range(self.x) for j in range(self.y)])
        raise TypeError

    def __add__(self, other):
        """ Метод Сложение матриц """
        if isinstance(self, Matrix) and isinstance(other, Matrix):
            if self.x == other.x and self.y == other.y:
                matrix_sum = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.y)] for i in range(self.x)]
                return Matrix(self.x, self.y, matrix_sum)
            raise ValueError
        raise TypeError

    def __mul__(self, other):
        """ Метод Умножение матрицы на число и на матрицу """
        if isinstance(self, Matrix) and isinstance(other, int | float):
            matrix_mul = [[self.matrix[i][j] * other for j in range(self.y)] for i in range(self.x)]
            return Matrix(self.x, self.y, matrix_mul)

        if isinstance(self, Matrix) and isinstance(other, Matrix):
            if self.y == other.x:
                # Индексы, используемые для определения размерности матриц: self:[m, n]; other:[n, k]
                matrix_mul = [[0 for _ in range(other.y)] for _ in range(self.x)]
                for m in range(self.x):
                    for k in range(other.y):
                        element = 0
                        for n in range(self.y):
                            element += self.matrix[m][n] * other.matrix[n][k]
                        matrix_mul[m][k] = element
                return Matrix(self.x, other.y, matrix_mul)
            raise ValueError
        raise TypeError

    def transposition(self):
        """ Метод Транспонирование матрицы """
        trans_matrix = list(zip(*self.matrix))
        return Matrix(self.y, self.x, trans_matrix)

    def show_matrix(self) -> None:
        """ Метод Вывод матрицы на экран """
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(f'{self.matrix[i][j]:>3}', end=' ')
            print()


if __name__ == '__main__':
    print('-----------------------------\nСОЗДАНИЕ СЛУЧАЙНОЙ МАТРИЦЫ:')
    i = randint(2, 5)
    j = randint(2, 5)
    init_matrix = Matrix(i, j)
    init_matrix.show_matrix()

    print('-----------------------------\nТРАНСПОНИРОВАНИЕ МАТРИЦЫ:')
    trans_matrix = init_matrix.transposition()
    trans_matrix.show_matrix()

    print('-----------------------------\nСЛОЖЕНИЕ И СРАВНЕНИЕ МАТРИЦ:')
    i = 3
    j = 4
    matrix_a = Matrix(i, j)
    matrix_a.show_matrix()
    print()
    matrix_b = Matrix(i, j)
    matrix_b.show_matrix()
    print('Результат сложения:')
    matrix_ab = matrix_a + matrix_b
    matrix_ab.show_matrix()

    print('матрицы равны?', end=' ')
    print(matrix_a == matrix_b)

    print('-----------------------------\nУМНОЖЕНИЕ МАТРИЦЫ НА ЧИСЛО:')
    i = randint(2, 5)
    j = randint(2, 5)
    matrix_a = Matrix(i, j)
    matrix_a.show_matrix()
    num = 3
    print(f'Результат умножения на {num}:')
    matrix_am = matrix_a * num
    matrix_am.show_matrix()

    print('-----------------------------\nУМНОЖЕНИЕ МАТРИЦЫ НА МАТРИЦУ:')
    # OK ===================================================
    # matrix_a = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
    # matrix_b = Matrix(3, 2, [[2, 3], [4, 5], [7, 9]])

    # matrix_a = Matrix(5, 2, [[1, -3], [1, 7], [0, 3], [4, 5], [2, 4]])
    # matrix_b = Matrix(2, 6, [[-9, 1, 0, 4, 1, 1], [-2, 2, -1, -2, 2, -1]])

    matrix_a = Matrix(4, 3, [[1, -2, 3], [4, 1, 7], [0, 1, 3], [1, 4, 5]])
    matrix_b = Matrix(3, 3, [[-9, 1, 0], [4, 1, 1], [-2, 2, -1]])
    # ======================================================

    matrix_a.show_matrix()
    print()
    matrix_b.show_matrix()
    print('Результат перемножения матриц:')
    matrix_axb = matrix_a * matrix_b
    matrix_axb.show_matrix()
