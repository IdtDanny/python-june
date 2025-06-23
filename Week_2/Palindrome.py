word = input('Enter Word: ')

if word == word[::-1]:
    print('Palindrome')
else:
    print('Not Palindrome')