average = float(input("Enter your average: "))
lgrade = float(input("Enter your Lowest Grade: "))

if average >= 80 and lgrade >= 80:
    print("First Class")
elif average >= 80 and lgrade >= 70:
    print("Second Upper Class A")
elif average >= 80 and lgrade <= 60:
    print("Second Lower Class A")
elif average >= 70 or lgrade >= 70:
    print("Second Upper Class B")
elif average >= 70 or lgrade < 60:
    print("Second Lower Class B")
elif average >= 60 and lgrade >= 50:
    print("Second Lower Class C")
elif average >= 60 and lgrade <= 50:
    print("Pass A")
elif average >= 50:
    print("Pass B")
else:
    print("Fail")