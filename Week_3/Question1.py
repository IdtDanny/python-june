student = {'Alice': 85, 'Ben': 92, 'Clara': 78, 'David': 90, 'Eva': 88, 'Frank': 75, 'Grace': 95, 'Henry': 67, 'Isla': 81, 'Jack': 89}

# Add a new student 'Karen' with score 83
student['Karen'] = 83

# Update Henry set score 72
student['Henry'] = 72

# Display all student scored above 80 (Passed Students)
print('Students with Score 80 or above: ')
for key in student:
    if student[key] >= 80:
        print(f'{key} : {student[key]}')

# Print name of one with the highest score
highestScore = student['Alice']
nameHighestScore = student['Alice']
for key in student:
    if student[key] > highestScore:
        highestScore = student[key]
        nameHighestScore = key

print(f'\nThe highest score is for {nameHighestScore} : {highestScore}')

# Average of the class
total = 0.0
average = 0.0
for key in student:
    total = total + student[key]

average = total / len(student)

average = round(average, 2)

print(f'The average is {average}')