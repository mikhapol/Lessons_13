class Rectangle:
    number = 0

    def __init__(self, width, length):
        self.width = width  # ширина
        self.length = length  # длина

        Rectangle.number += 1

    def perimeter(self):
        """
        Метод perimeter() для вычисления периметра прямоугольника.
        """
        return (self.width + self.length) * 2

    def area(self):
        """
        Метод area() для вычисления площади прямоугольника.
        """
        return self.width * self.length

    def display_print(self):
        print(f'Прямоугольник с шириной: {self.width} и длиной: {self.length}\n'
              f'Периметр: {self.perimeter()}\n'
              f'Площадь: {self.area()}')

    def display_return(self):
        return f'Прямоугольник с шириной: {self.width} и длиной: {self.length}\n' \
               f'Периметр: {self.perimeter()}\n' \
               f'Площадь: {self.area()}'


r1 = Rectangle(7, 8)
r2 = Rectangle(10, 20)
# print(f'Ширина: {r1.width}\nДлина: {r1.length}')
# print('Периметр:', Rectangle.perimeter(r1))
# print('Площадь:', Rectangle.area(r1))
Rectangle.display_print(r1)
Rectangle.display_print(r2)
print("--------------")
print(r1.display_return())
print(r2.display_return())
print('Всего =', Rectangle.number)
