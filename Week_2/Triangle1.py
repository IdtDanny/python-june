import math

a = float(input('Enter 1st Side: '))
b = float(input('Enter 2nd Side: '))
angle1 = float(input('Enter one angle: '))

# c2 = a2 + b2 - 2ab.cosC

a2 = math.pow(a,2)
b2 = math.pow(b, 2)
cosC = math.cos(math.radians(angle1))
ab = 2 * a * b * cosC

c2 = a2 + b2 - ab

c = math.sqrt(c2)

print(f'Side c: {c}')

# cosA = (b2 + c2 - a2)/2bc

cosA = (b2 + c2 - a2) / (2 * b * c)

angle2 = math.degrees(math.acos(cosA))

print(f'Angle A: {angle2}')

# cosB = (c2 + a2 - b2)/2ac

cosB = (c2 + a2 - b2) / (2 * a * c)

angle3 = math.degrees(math.acos(cosB))

print(f'Angle B: {angle3}')