name = input('Enter name to see the ASCII Sum: ')

sumAscii = 0
asciiCode = {}

for i in name:
    asciiCode[i] = ord(i)
    sumAscii += ord(i)

print(f'The ASCII Code Dict for {name} : \n{asciiCode} \nThe Equivalent Sum is {sumAscii}')