def check_voting_eligibility(name, age):
    if age >= 120 or age < 0:
        return f'Error! Invalid age: {age} years old'
    else:
        if age >= 18:
            return f'Welcome {name}, you are eligible to vote!'
        else:
            return f'Remain {18 - age} years to be eligible'

print(check_voting_eligibility(input('Name: '), int(input('Age: '))))