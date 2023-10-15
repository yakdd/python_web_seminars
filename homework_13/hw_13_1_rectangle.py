# Добавьте в задачу Rectangle, которую писали ранее, исключение NegativeValueError,
# которое выбрасывается при некорректных значениях ширины и высоты,
# как при создании объекта, так и при установке их через сеттеры.
class NegativeValueError(Exception):
    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return f'{self.msg}'


class Rectangle:
    """ Класс Прямоугольник """

    def __init__(self, a, b=None):
        if a <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {a}')
        if b is not None and b <= 0:
            raise NegativeValueError(f'Высота должна быть положительной, а не {b}')
        self.height = a
        self.width = b if b else a

    def perimeter(self) -> int:
        """ Периметр прямоугольника """
        return 2 * (self.width + self.height)

    def area(self) -> int:
        """ Площадь прямоугольника """
        return self.width * self.height

    def __add__(self, other) -> object:
        """ Сложение прямоугольников """
        if isinstance(other, Rectangle):
            length = self.width + other.width
            width = self.height + other.height
            return Rectangle(width, float(length))
        raise TypeError

    def __sub__(self, other) -> object:
        """ Вычитание прямоугольников """
        if isinstance(other, Rectangle):
            length = self.width - other.width
            width = self.height - other.height
            if length > 0 and width > 0:
                return Rectangle(width, float(length))
        raise TypeError

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        raise TypeError

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() > other.area()
        raise TypeError

    def __ge__(self, other):
        if isinstance(other, Rectangle):
            return self.area() >= other.area()
        raise TypeError

    def __repr__(self):
        return f'Rectangle({self.height}, {self.width})'

    def __str__(self):
        return f'Прямоугольник со сторонами {self.height} и {self.width}'


if __name__ == '__main__':
    # rect = Rectangle(10)
    # print(rect)

    # 1 --------------------------------
    # r = Rectangle(-2)       # __main__.NegativeValueError: Ширина должна быть положительной, а не -2

    # 2 --------------------------------
    r = Rectangle(5, -3)  # __main__.NegativeValueError: Высота должна быть положительной, а не -3

    # rect1 = Rectangle(4, 5)
    # rect2 = Rectangle(3, 3)
    #
    # print(rect1)
    # print(rect2)
    #
    # print(rect1.perimeter())
    # print(rect1.area())
    # print(rect2.perimeter())
    # print(rect2.area())
    #
    # rect_sum = rect1 + rect2
    # rect_diff = rect1 - rect2
    #
    # print(rect_sum)
    # print(rect_diff)
    #
    # print(rect1 < rect2)
    # print(rect1 == rect2)
    # print(rect1 <= rect2)
    #
    # print(repr(rect1))
    # print(repr(rect2))
