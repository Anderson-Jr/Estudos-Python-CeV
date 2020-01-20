phrase = input('Enter a phrase: ').strip().upper()
reverse = phrase[::-1]
if phrase == reverse:
    print('The phrase is a palindrome!')
else:
    print('The phrase is not a palindrome!')
