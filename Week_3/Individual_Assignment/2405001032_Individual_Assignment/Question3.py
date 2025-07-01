class Animal:
    def __init__(self, name, age, adoption_status):
        self.name = name
        self.age = age
        self.adoption_status = adoption_status

class dogs(Animal):
    def __init__(self, name, age, adoption_status, breed):
        super().__init__(name, age, adoption_status)
        self.breed = breed

    def is_trained(self):
        return 'Ready for Adoption'
        
class cats(Animal):
    def __init__(self, name, age, adoption_status, color):
        super().__init__(name, age, adoption_status)
        self.color = color

    def like_to_be_held(self):
        return 'Only for experienced owners if they don’t like to be held'

dog = dogs('Bob', 2, 'Unknown', 'Hybrid')

print(dog.is_trained())