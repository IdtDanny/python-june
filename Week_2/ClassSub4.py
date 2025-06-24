class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2


length = float(input('Enter the length: '))
width = float(input('Enter the width: '))

rect = Rectangle(length, width)

print(f'The area is {rect.area()} \nThe perimeter is {rect.perimeter()}')