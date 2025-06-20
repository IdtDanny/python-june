class student:
    def __init__(self, firstName, lastName, module, session):
        self.firstName = firstName
        self.lastName = lastName
        self.module = module
        self.session = session

stud1 = student('Danny', 'Idukundatwese', 'Python', 'Evening')

print(f'{stud1.firstName} {stud1.lastName} \n{stud1.module} \n{stud1.session}')
