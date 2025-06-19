print('Learn Alphabets, Enter the alphabet you see: ')

start = 65

alpha = ord(input(f'{chr(start)} : '))

while alpha < 255: # Iterate through whole ASCII Table Elements
    if alpha < 65 + 25  and start < 65 + 25: # Limit until the last UpperCase element 'Z'
        if start == alpha:
            alpha = ord(input(f'{chr(alpha + 1)} : '))
            start += 1
        else:
            print('Invalid Alphabet! Not the Same!')
            alpha = ord(input(f'{chr(start)} : '))
    elif alpha == 65 + 25:
        print('Success!')
        break
    else:
        print('Invalid Alphabet! Not the Same!')
        alpha = ord(input(f'{chr(start)} : '))