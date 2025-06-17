a = 97
while a <= 97 + 25:
    a = input(f'{chr(a)} : ')
    if a != a:
        a -= 1
    a = ord(a) + 1