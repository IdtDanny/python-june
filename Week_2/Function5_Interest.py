# Simple Interest
def Interest(deposit, rate, time):
    return deposit * rate * time * 0.01

deposit = int(input("Enter the deposit amount: "))
rate = float(input("Enter the interest rate in %: "))
time = int(input("Enter the time in year: "))

interest = Interest(deposit, rate, time)
print(f'The Simple Interest is {interest}')