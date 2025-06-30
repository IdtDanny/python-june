# Enter the word to check
word = input('Enter a word to check if palindrome: ')

# reverse the word
reverse = word[::-1]

# Check if the word equal to the reverse
if reverse == word:
    print(f'The word {word} is palindrome')
else:
    print(f'The word {word} is not palindrome')