class student:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

class intake(student):
    def __init__(self, firstName, lastName, module, session, intake):
        super().__init__(firstName, lastName)
        self.module = module
        self.session = session
        self.intake = intake

class Payment(intake):
    def __init__(self, firstName, lastName, module, session, intake, payment):
        super().__init__(firstName, lastName, module, session, intake)
        self.payment = payment

    def fee(self):
        if self.payment < 100000:
            return self.payment * 2
            # return f'{self.payment * 2} | Penalty of {self.payment}'
        else:
            return self.payment


stud1 = Payment('Shivan', 'Sh', 'Python', 'Evening', 'January', 90000)
stud2 = Payment('Shamir', 'Sh', 'Python', 'Evening', 'January', 200000)

# stud2 = Payment('Danny', 'Idukundatwese', 'Python', 'Evening', 'January', 0)
# stud2.payment = int(input('Enter payment: '))

print(f'FullName: {stud1.firstName} {stud1.lastName} \nModule: {stud1.module} \nSession: {stud1.session} \nIntake: {stud1.intake} \nPayment: {stud1.fee()}')
print(f'\nFullName: {stud2.firstName} {stud2.lastName} \nModule: {stud2.module} \nSession: {stud2.session} \nIntake: {stud2.intake} \nPayment: {stud2.fee()}')