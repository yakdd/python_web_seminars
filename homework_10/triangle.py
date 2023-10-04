from random import randint


class Triangle:

    def __init__(self, side_a: int, side_b: int, side_c: int):
        if self.check_data([side_a, side_b, side_c]):
            self.side_a = side_a
            self.side_b = side_b
            self.side_c = side_c
        else:
            print('Треугольника с такими сторонами не существует!')
            exit()

    @staticmethod
    def check_data(sides: list):
        for side in sides:
            if (sum(sides) - side) <= side:
                return False
        return True

    def __str__(self) -> str:
        triangle_sides = {self.side_a, self.side_b, self.side_c}
        if len(triangle_sides) == 1:
            return f'Это равносторонний треугольник со сторонами {self.side_a}, {self.side_b}, {self.side_c}'
        elif len(triangle_sides) == 2:
            return f'Это равнобедренный треугольник со сторонами {self.side_a}, {self.side_b}, {self.side_c}'
        else:
            return f'Это треугольник со сторонами {self.side_a}, {self.side_b}, {self.side_c}'

    def perimeter(self) -> int:
        return self.side_a + self.side_b + self.side_c

    def area(self) -> float:
        p = self.perimeter() / 2
        area = (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5
        return area


if __name__ == '__main__':
    sides = [randint(1, 10) for _ in range(3)]
    triangle = Triangle(*sides)
    print(triangle)
    print(f'{triangle.perimeter() = }')
    print(f'{triangle.area() = }')
