def Rectangle(width, length):
    return width * length, (width + length) * 2

width = float(input(f'Enter width: '))
length = float(input(f'Enter length: '))

area, perimeter = Rectangle(width, length)

print(f'The area is {area} \nThe perimeter is  {perimeter}')