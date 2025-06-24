age = int(input('Enter your age: '))
experience = int(input('Enter years of experience: '))
highschool = input('Have you completed high school? Yes/No: ')
employment = input('Were you employed for the past year? Yes/No: ')
criminal = input('Do you have an criminal record? Yes/No: ')

if age >= 18:
    if experience >= 2:
        if criminal != 'Yes':
            if highschool == 'Yes':
                if employment == 'Yes':
                    print('Eligible')
                else:
                    print('Needs Further Review')
            else:
                print('Not Eligible')
        else:
            print('Not Eligible')
    else:
        print('Needs Further Review')
else:
    print('Not Eligible')