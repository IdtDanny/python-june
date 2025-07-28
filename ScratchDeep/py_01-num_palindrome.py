num = int(input('Enter number to check: '))

temp = num; rev = int(0)

if (num <= 0):
    print('Invalid Number!')
else:
    while (num != 0):
        last_digit = num % 10
        rev = (rev * 10) + last_digit
        num = int(num / 10)
    if (temp == rev):
        print(f'{temp} is a palindrome, it\'s reverse is {rev}')
    else:
        print(f'{temp} is not palindrome, it\'s reverse is {rev}')