class Rectangle():
    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height}'

    def set_width(self, width):
        self.width = int(width)

    def set_height(self, height):
        self.height = int(height)

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        sides = [f'*{" " * self.width - 2}*' for i in range(self.height - 2)]
        return '\n'.join(['*' * self.width], sides, ['*' * self.width])

    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
    
    def __str__(self):
        return f'Square(side={self.width}'

    def set_side(self, length):
        self.width = length
        self.height = length

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
