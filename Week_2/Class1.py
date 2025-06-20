class animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog = animal("Dog", 20)

print(dog.age)