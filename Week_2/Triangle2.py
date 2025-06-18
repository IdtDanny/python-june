import math

angleA = float(input('Enter angle A: '))
angleB = float(input('Enter angle B: '))
sideB = float(input('Enter side B: '))

# Sine rule
# a / sinA = b / sinB = c / sinC
# a = b.sinA / sinB

# Test with A = 37, B=53, C=90, a=3, b=4, c = 5, Area = 6

sideA = sideB * math.sin(math.radians(angleA)) / math.sin(math.radians(angleB))

angleC =  180 - (angleA + angleB)

sideC = sideB * math.sin(math.radians(angleC)) / math.sin(math.radians(angleB))

area = 0.5 * sideA * sideB * math.sin(math.radians(angleC))

print(f'Side A is {sideA} \nSide B is {sideB} \nSide C is {sideC} \nAngle A is {angleA}')
print(f'Angle B is {angleB} \nAngle C is {angleC} \nArea is {area}')