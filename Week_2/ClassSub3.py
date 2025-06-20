class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car1 = Car

car1.make = input('What is your car make? ')
car1.model = input('What is your car model? ')
car1.year = input('What is your car year? ')

print(car1.make)