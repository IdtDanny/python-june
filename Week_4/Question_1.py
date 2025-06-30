import math

def prime(num):
    if num < 2:
        return False
    elif num > 3:
        if num % math.sqrt(num) == 0:
            return False
        elif num % 2 == 0:
            return False
        else:
            d = None
            for n in range(2, num, 1):
                if num % (n + 1) == 0:
                    d = False
                else:
                    d = True
                return d
    else:
        return True

primeNumber = []

limit = int(input('Enter the limit: '))

for i in range(1, limit):
    if prime(i) == True:
        primeNumber.append(i)

print(primeNumber)