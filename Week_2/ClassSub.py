class animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class domestic(animal):
    def __init__(self, name, age, owner):
        # animal.__init__(self, name, age)
        super().__init__(name, age)
        self.owner = owner

    def ranking(self):
        if self.age < 1.5:
            return 'Under 2.5'
        else:
            return 'Above 1.5'

goat = domestic('Ruhaya', 1, 'Noheri')

print(f'{goat.name} aged {goat.age} years old belongs to {goat.owner}. \n{goat.ranking()}')