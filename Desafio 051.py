term = int(input('Enter the first term: '))
reason = int(input('Enter the reason of Arithmetic Progression: '))
for c in range(1, 11):
    print(f'The {c}th term of Arithmetic Progression is {term}')
    term += reason
