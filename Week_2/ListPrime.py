limit = int(input('Enter the limit to list: '))

prime = []

start = 2

while start <= limit:
    for i in range(2, start):
        if start % i == 0:
            break
    else:
        prime.append(start)
    start += 1

print(prime)