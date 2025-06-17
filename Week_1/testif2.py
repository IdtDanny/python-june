num = int(input("Enter a number: "))

if num % 3 == 0:
    if num % 5 == 0:
        print(f"{num} is divisible by 3 and 5")
    else:
        print(f"{num} is not divisible by 5")
else:
    print(f"{num} is not divisible by 3")