word = input('Enter the word to check: ')

if word == word[len(word)::-1]:
    print('Palindrome')
else:
    print('Not Palindrome')