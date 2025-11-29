key = int(input("Enter the Key for Caesar's Cipher: "))

if 0 < key <= 25:
    i = int(65)
    while i < 65 + 26:
        print(f'{chr(i)}', end=' | ')
        i = i + 1

    j = int(65) + key
    print()
    while j < 65 + 25 + key:
        if j == 65 + 26:
            k = int(0)
            while k < key:
                print(f'{chr(k + 65)}', end=' | ')
                k = k + 1
        elif j > 65 + 25:
            break
        print(f'{chr(j)}', end=' | ')
        j = j + 1
else:
    print(f'Invalid input key = {key}', end='')
