choice = int(input('Enter 1 for minutes and 0 for hours: '))

price = int(0)

if (choice == 1):
    hours = int(input('Enter hours spent: '))

    if (hours <= 1):
        price = 500
    if(1 < hours < 3):
        price = 1000
    else:
        price = 1000
        for i in range(hours):
            if (i >= 3):
                price = price + 500
    print(f'You will be charged: {price} RWF')
if (choice == 0):
    price = 300
    print(f'You will be charged: {price} RWF')
else: 
    print('Invalid choice!')