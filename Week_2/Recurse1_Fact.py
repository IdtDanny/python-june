def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

x = int(input('Enter a number: '))
print(f'The factorial of {x} is {factorial(x)}')