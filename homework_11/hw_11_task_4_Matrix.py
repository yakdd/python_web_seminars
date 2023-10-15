from random import randint


class Matrix:
    """ Класс Матрица """

    def __init__(self, x: int, y: int, matrix_list=None):
        self.x = x
        self.y = y
        if not matrix_list:
            self.matrix = [[0 for _ in range(self.y)] for _ in range(self.x)]
        else:
            self.matrix = matrix_list

    @property
    def data(self):
        return self.matrix

    @data.setter
    def data(self, matrix_list):
        self.matrix = [[matrix_list[i][j] for j in range(len(matrix_list[i]))] for i in range(len(matrix_list))]

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

    def __str__(self) -> str:
        matrix_string = ''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if j == len(self.matrix[i]) - 1:
                    matrix_string += str(self.matrix[i][j])
                else:
                    matrix_string += str(self.matrix[i][j]) + ' '
            matrix_string += '\n'
        return matrix_string[:-1]


# Создаем матрицы
matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

# Выводим матрицы
print(matrix1)

print(matrix2)

# Сравниваем матрицы
print(matrix1 == matrix2)

# Выполняем операцию сложения матриц
matrix_sum = matrix1 + matrix2
print(matrix_sum)

# Выполняем операцию умножения матриц
matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5, 6]]

matrix4 = Matrix(2, 2)
matrix4.data = [[7, 8], [9, 10]]

result = matrix3 * matrix4
print(result)
