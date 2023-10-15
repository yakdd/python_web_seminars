from random import randint


class Matrix:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.matrix = [[randint(0, 9) for _ in range(self.y)] for _ in range(self.x)]
        self.print_matrix(self.matrix, 'init')

    def transposition(self):
        trans_matrix = list(zip(*self.matrix))
        self.print_matrix(trans_matrix, 'trans')
        return trans_matrix

    @staticmethod
    def print_matrix(matrix: list, type_matrix: str):
        print(f'{type_matrix}-matrix:')
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print(matrix[i][j], end=' ')
            print()

    def __repr__(self):
        return f'Matrix({self.x}, {self.y})'


if __name__ == '__main__':
    i = randint(2, 5)
    j = randint(2, 5)
    new_matrix = Matrix(i, j)
    print(new_matrix)
    print(type(new_matrix))
    new_matrix.transposition()
