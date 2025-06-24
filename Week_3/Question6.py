def transaction(name, balance):

    choice = int(input('Choose: \n1. Deposit \n2. Withdraw \n3. Check Balance \n'))

    if choice == 1:
        deposit = int(input('Enter amount to deposit: '))
        return balance + deposit

    elif choice == 2:
        withdraw = int(input('Enter amount to withdraw: '))
        if balance >= withdraw:
            return f'Remain {balance - withdraw}'
        else:
            return 'Insufficient Balance'

    elif choice == 3:
        return f'Your current balance is {balance}'

    else:
        return 'Wrong Choice'

name = input('Enter your name: ')
currentBalance = int(input('Enter your current balance: '))
print(transaction(name, currentBalance))
