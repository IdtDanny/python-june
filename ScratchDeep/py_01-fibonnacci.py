num = []

size = int(input('Enter size of your fibonnacci: '))

num.append(0)
num.append(1)

for i in range(size):
    if (i > 1):
        num_fib = num[i-1] + num[i-2]
        num.append(num_fib)

print(num)