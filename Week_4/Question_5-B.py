principle = int(input("Enter the Principle Amount (P): "))
rate = float(input("Enter the rate (R): "))
time = int(input("Enter the time (T) in year: "))

simpleInterest = lambda interest: principle * rate * time * 0.01

print(f'The Simple Interest is {simpleInterest(interest = principle)}')