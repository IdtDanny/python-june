student = {
    "Name" : "Muhayi",
    "Class" : "Evening",
    "Subjet" : "Python"
}

print(student)
print(student['Name'])

student["Duration"] = 180

for keys, values in student.items():
    print(f"{keys} : {values}")