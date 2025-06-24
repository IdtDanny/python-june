class Staff:
    def __init__(self, name, staff_id, department):
        self.name = name
        self.staff_id = staff_id
        self.department = department

class Teacher(Staff):
    def __init__(self, name, staff_id, department, subject, teaching_hours):
        super().__init__(name, staff_id, department)
        self.subject = subject
        self.teaching_hours = teaching_hours

    def overload(self):
        if self.teaching_hours > 20:
            return 'Overload'
        return 'Not Overload'


class Administrator(Staff):
    def __init__(self, name, staff_id, department, position, office_hours):
        super().__init__(name, staff_id, department)
        self.position = position
        self.office_hours = office_hours

    def mark(self):
        if self.office_hours > 40:
            return 'Senior'
        return 'Not Senior'

teach = Teacher('Danny', '24', 'ICT', 'Python', 10)

print(f'{teach.name}, {teach.staff_id}, {teach.department}, {teach.subject}, {teach.overload()}')

admin = Administrator('tifa','25','fina','hod',20)

print(f'{admin.name},{admin.staff_id},{admin.department},{admin.position},{admin.office_hours},{admin.mark()}')