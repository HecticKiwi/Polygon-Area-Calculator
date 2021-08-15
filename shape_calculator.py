class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def def_width(self, width):
        self.width = width

    def def_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        sides = [f'*{" " * self.width - 2}*' for i in range(self.height) - 2]
        return '\n'.join(['*' * self.width], sides, ['*' * self.width])

    

