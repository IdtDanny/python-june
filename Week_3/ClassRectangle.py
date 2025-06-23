class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

class Square(Rectangle):
    def __init__(self, width, length):
        super().__init__(width, length)

    def check(self):
        if self.width == self.length:
            return 'It\'s Square'
        else:
            return 'It\'s Rectangle'

square = Square(int(input(f'Enter width: ')), int(input(f'Enter Length: ')))

print(square.check())