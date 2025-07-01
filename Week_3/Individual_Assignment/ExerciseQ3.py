class Animal():
    def __init__(self,name,age,adoption_status):
        self.name=name
        self.age=age
        self.adoption_status=adoption_status
class Dog(Animal):
    def __init__(self,name,age,adoption_status,breed,trained):
        super().__init__(name,age,adoption_status)
        self.breed=breed
        self.trained=trained
    def check_adoption(self):
        if self.trained=="yes":
            return 'ready for adoption'
        else:
            return 'not ready for adoption'
class Cat(Animal):
    def __init__(self,name,age,adoption_status,color,like_to_be_held):
        super().__init__(name,age,adoption_status)
        self.color=color
        self.like_to_be_held=like_to_be_held
    def check_like_to_be_held(self):
        if self.like_to_be_held=="No":
            return 'for experienced owners'
        else:
            return 'Likes to be held'
D1=Dog('doggy',1,'no','have breed','yes')
C1=Cat('cat',1,'yes','white','yes')
print(f'The Dos is {D1.check_adoption()}')
print(f'The Cat {C1.check_like_to_be_held()}')
