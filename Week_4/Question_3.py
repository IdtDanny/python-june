loanAmount = float(input("Enter loan amount: "))

repaymentAmount = float(input("Enter monthly repayment amount: "))

numberOfMonths = int(input("Enter number of months for repayment: "))

for i in range(1, numberOfMonths + 1):
    if loanAmount >= repaymentAmount:
        loanAmount -= repaymentAmount
    else:
        repaymentAmount = loanAmount
        loanAmount -= repaymentAmount
    print(f'Paid {repaymentAmount} for month {i}, The remain amount is {loanAmount}')