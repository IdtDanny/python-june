end = 30

prime = []

start = 2

while start <= end:

    for i in range(3, start):
        if start % i == 0:
            break

        elif start % 2 == 0:
            break

    else:
        prime.append(start)

    start = start + 1

print(prime)