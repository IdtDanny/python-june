import math

sideA = float(input('Enter Side A: '))
sideB = float(input('Enter Side B: '))
angleC = float(input('Enter angle C: '))

# Cosine Rule:  c2 = a2 + b2 - 2ab.cosC
# Test with A = 37, B=53, C=90, a=3, b=4, c = 5, Area = 6

c2 = math.pow(sideA, 2) + math.pow(sideB, 2) - (2 * sideA * sideB * math.cos(math.radians(angleC)))

sideC = math.sqrt(c2)

sin_angleB = sideB * math.sin(math.radians(angleC)) / sideC

angleB = math.degrees(math.asin(sin_angleB))

angleA = 180 - (angleB + angleC)

print(f'Side C: {sideC} \nAngle A: {angleA} \nAngle B: {angleB} \nAngle C: {angleC}')

print(f'The area is: {sideA * sideC * sin_angleB * 0.5}')