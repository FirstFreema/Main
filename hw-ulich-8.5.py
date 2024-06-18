# 1
import math

class Figure:
    def __init__(self, name):
        self.name = name

    def calculate_area(self):
        pass

class Rectangle(Figure):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Circle(Figure):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

class RightTriangle(Figure):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

class Trapezoid(Figure):
    def __init__(self, name, base1, base2, height):
        super().__init__(name)
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def calculate_area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

# Example
rectangle = Rectangle("Прямоугольник", 5, 10)
print(f"Площадь {rectangle.name}: {rectangle.calculate_area()}")
circle = Circle("Круг", 7)
print(f"Площадь {circle.name}: {circle.calculate_area()}")
right_triangle = RightTriangle("Прямоугольный треугольник", 6, 8)
print(f"Площадь {right_triangle.name}: {right_triangle.calculate_area()}")
trapezoid = Trapezoid("Трапеция", 4, 8, 5)
print(f"Площадь {trapezoid.name}: {trapezoid.calculate_area()}")

# 2
class Figure:
    def __init__(self, name):
        pass

    def square(self):
        pass

    def __int__(self):
        return int(self.square())

    def __str__(self):
        return f"Фигура: {type(self).__name__}, Площадь: {self.square()}"

class Rectangle(Figure):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height

class Circle(Figure):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2

class RightTriangle(Figure):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height

    def square(self):
        return 0.5 * self.base * self.height

class Trapezoid(Figure):
    def __init__(self, name, base1, base2, height):
        super().__init__(name)
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def square(self):
        return 0.5 * (self.base1 + self.base2) * self.height

# Example
rectangle = Rectangle("Прямоугольник", 5, 10)
print(rectangle)
print(int(rectangle))
circle = Circle("Круг", 7)
print(circle)
print(int(circle))
right_triangle = RightTriangle("Прямоугольный треугольник", 6, 8)
print(right_triangle)
print(int(right_triangle))
trapezoid = Trapezoid("Трапеция", 4, 8, 5)
print(trapezoid)
print(int(trapezoid))

