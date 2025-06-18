def mathOps(a,b):
    return a+b, a-b, a*b, a/b, a%b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum, diff, product, div, mod = mathOps(num1, num2)

print(f'Sum: {sum}, \nDifference: {diff}, \nProduct: {product}, \nQuotient: {div}, \nRemainder: {mod}')
