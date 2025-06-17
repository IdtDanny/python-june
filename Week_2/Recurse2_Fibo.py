def fib(num):
    if num < 2:
        return num
    return fib(num - 1) + fib(num - 2)

x = int(input('Enter limit: '))

list = []

for i in range(x):
    list.append(fib(i))

print(list)