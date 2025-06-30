class lecturer:
    def __init__(self, firstname, surname, email, salary):
        self.firstname = firstname
        self.surname = surname
        self.email = firstname + '.' + surname + '@havard.ac.us'
        self.salary = salary

    def display(self):
        print(f'Full name: {self.firstname} {self.surname} \nEmail: {self.email}')

    def updateSalary(self):
        self.salary = self.salary + (self.salary * 0.1)

class Permanent_residence(lecturer):
    def __init__(self, firstname, surname, email, salary, nationality):
        super().__init__(firstname, surname, email, salary)
        self.nationality = nationality

class Senior_lecturer(lecturer):
    def __init__(self, firstname, surname, email, salary, yearsOfExperience):
        super().__init__(firstname, surname, email, salary)
        self.yearsOfExperience = yearsOfExperience

        if yearsOfExperience > 5:
            self.salary = self.salary + (self.salary * 0.5)

lecturer_2 = Senior_lecturer('Peter', 'Okolo', '<EMAIL>', 20000, 7)

lecturer_2.display()

print(f'\nThe salary of Senior Lecturer with 50% increase is {lecturer_2.salary}')

lecturer_2.updateSalary()

print(f'After update the Salary of Senior Lecturer with 10% is {lecturer_2.salary}')