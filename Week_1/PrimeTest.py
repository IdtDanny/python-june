# Request user to enter the limit number
num = int(input('Enter a number: '))

# Make a sample list
prime = []

# Set starting point for prime numbers
k = 2

# Iterate through to add the list
while k <= num:

    # Loop through the numbers below the set
    for i in range(3, k):

        # Should it be divisible by lesser number then break
        if k % i == 0:
            break

        # Should it be divisible by 2 ex. 4
        elif k % 2 == 0:
            break

    # Otherwise you append in the list
    else:
        prime.append(k)

    # Increment
    k = k + 1

# Display the list
print(prime)