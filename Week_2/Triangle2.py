import math

angleA = float(input('Enter angle A: '))
angleB = float(input('Enter angle B: '))
sideB = float(input('Enter side B: '))



sideA = sideB * math.sin(math.radians(angleA)) / math.sin(math.radians(angleB))

angleC =  180 - (angleA + angleB)

sideC = sideB * math.sin(math.radians(angleC)) / math.sin(math.radians(angleB))

area = 0.5 * sideA * sideB * math.sin(math.radians(angleC))

print(f'Side A is {sideA} \nSide B is {sideB} \nSide C is {sideC} \nAngle A is {angleA}')
print(f'Angle B is {angleB} \nAngle C is {angleC} \nArea is {area}')