import math

sideA = int(input('Enter side a: '))
sideB = int(input('Enter side b: '))
angleB = int(input('Enter angle B: '))

# sideC, angleA, angleC

sinA = (sideA * math.sin(math.radians(angleB))) / sideB

angleA = math.degrees(math.asin(sinA))

angleC = 180 - (angleA + angleB)
print(angleA)