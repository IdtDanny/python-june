modules = {'Python': 0.0, 'ICT': 0, 'Cryptograph': 0.0, 'Operations Research': 0.0, 'Linear Algebra' : 0.0}

total = 0

maximum = modules['Python']
max_module = modules['Python']

for key, values in modules.items():
    modules[key] = float(input(f'{key} : '))
    total += modules[key]
    if maximum < modules[key]:
        maximum = modules[key]
        max_module = key


average = total / 5

print(f'\nThe average is {average} %')

if average < 100:
    if average > 80:
        print('A (Excellent)')
    elif 70 <= average < 80:
        print('B (Very Good)')
    elif 60 <= average < 70:
        print('C (Good)')
    elif 50 <= average < 60:
        print('D (Pass)')
    else:
        print('F (Fail)')
else:
    print('Out of range')

print(f'The maximum marks is {maximum} % for {max_module}')