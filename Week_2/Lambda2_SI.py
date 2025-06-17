deposit = int(input("Enter the deposit: "))
rate = float(input("Enter the rate in %: "))
time = int(input("Enter the time in year: "))

interest = lambda principle: deposit * rate * time * 0.01

print(interest(principle = deposit))