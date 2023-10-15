# Класс Rectangle - работа с прямоугольниками
# Разработайте программу для работы с прямоугольниками. Необходимо создать класс Rectangle,
# который будет представлять прямоугольник с заданными шириной и высотой.
#
# Класс Rectangle должен иметь следующие атрибуты и методы:
# Атрибуты:
# - width (int): ширина прямоугольника.
# - height (int): высота прямоугольника.
# Методы:
# - perimeter(): метод для вычисления периметра прямоугольника. Возвращает периметр как целое число.
# - area(): метод для вычисления площади прямоугольника. Возвращает площадь как целое число.
# - __add__(other): метод, позволяющий складывать два прямоугольника.
# Возвращает новый прямоугольник с шириной и высотой, равными сумме соответствующих атрибутов исходных прямоугольников.
# __sub__(other): метод, позволяющий вычитать один прямоугольник из другого.
# Возвращает новый прямоугольник с шириной и высотой, равными разности соответствующих атрибутов исходных прямоугольников.
# __lt__(other): метод, определяющий, является ли текущий прямоугольник меньше по площади, чем другой прямоугольник.
# Возвращает True, если площадь текущего прямоугольника меньше площади другого, и False в противном случае.
# __eq__(other): метод, определяющий, равны ли два прямоугольника по площади.
# Возвращает True, если площади равны, и False в противном случае.
# __le__(other): метод, определяющий, меньше или равен текущий прямоугольник по площади, чем другой прямоугольник.
# Возвращает True, если площадь текущего прямоугольника меньше или равна площади другого, и False в противном случае.
# __str__(): метод для получения строкового представления прямоугольника.
# Возвращает строку с информацией о ширине и высоте прямоугольника.
# __repr__(): метод для получения строкового представления прямоугольника, которое может быть использовано
# для создания нового объекта.
#
# Пример использования:
# На входе:
# rect1 = Rectangle(5, 10)
# rect2 = Rectangle(3, 7)
#
# print(f"Периметр rect1: {rect1.perimeter()}")
# print(f"Площадь rect2: {rect2.area()}")
# print(f"rect1 < rect2: {rect1 < rect2}")
# print(f"rect1 == rect2: {rect1 == rect2}")
# print(f"rect1 <= rect2: {rect1 <= rect2}")
#
# rect3 = rect1 + rect2
# print(f"Периметр rect3: {rect3.perimeter()}")
# rect4 = rect1 - rect2
# print(f"Ширина rect4: {rect4.width}")
#
# На выходе:
# Периметр rect1: 30
# Площадь rect2: 21
# rect1 < rect2: False
# rect1 == rect2: False
# rect1 <= rect2: False
# Периметр rect3: 50.0
# Ширина rect4: 2
class Rectangle:
    """ Класс Прямоугольник """

    def __init__(self, a, b=None):
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
            return Rectangle(width, length)
        raise TypeError

    def __sub__(self, other) -> object:
        """ Вычитание прямоугольников """
        if isinstance(other, Rectangle):
            length = self.width - other.width
            width = self.height - other.height
            if length > 0 and width > 0:
                return Rectangle(width, length)
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
    rect1 = Rectangle(4, 5)
    rect2 = Rectangle(3, 3)

    print(rect1)
    print(rect2)

    print(rect1.perimeter())
    print(rect1.area())
    print(rect2.perimeter())
    print(rect2.area())

    rect_sum = rect1 + rect2
    rect_diff = rect1 - rect2

    print(rect_sum)
    print(rect_diff)

    print(rect1 < rect2)
    print(rect1 == rect2)
    print(rect1 <= rect2)

    print(repr(rect1))
    print(repr(rect2))
