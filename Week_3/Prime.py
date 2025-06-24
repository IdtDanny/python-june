end = int(input('Enter the limit number: '))

prime = []

start = 2

while start < end:
    for k in range(2, start):
        if start % k == 0:
            break
    else:
        prime.append(start)
    start += 1

print(prime)