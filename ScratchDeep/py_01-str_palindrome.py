word = input('Enter string to check: ')
size = len(word)
beg = int(0); end = int(size - 1); mid = int((end - beg) / 2); flag = int(0)

if (size <= 0):
    print ('Invalid word!')

while (size >= 0):
    if (word[beg] == word[end]):
        beg = beg + 1
        end = end - 1
        mid = int((end - beg) / 2)
        size = mid
        flag = 1
    else:
        size = -1
        flag = 0
if (flag == 1):
    print(f'{word} is palindrome')
else:
    print(f'{word} is not palindrome')