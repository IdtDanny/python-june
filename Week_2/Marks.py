modules = {'Python': 0, 'ICT': 0, 'Cryptograph': 0, 'Operations Research': 0, 'Linear Algebra' : 0}

total = 0

maximum = modules['Python']
max_module = modules['Python']

for key, values in modules.items():
    modules[key] = float(input(f'{key} : '))
    total += modules[key]
    if maximum < modules[key]:
        maximum = modules[key]

average = total / 5

print(f'\nThe average is {average} %')

if average < 100:
    if average > 80:
        print('A (Excellent)')
    elif average >= 70 and average < 80:
        print('B (Very Good)')
    elif average >= 60 and average < 70:
        print('C (Good)')
    elif average >= 50 and average < 60:
        print('D (Pass)')
    else:
        print('F (Fail)')
else:
    print('Out of range')

print(f'The maximum is {maximum} %')