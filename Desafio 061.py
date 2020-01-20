term = int(input('Enter the first term: '))
reason = int(input('Enter the reason of Arithmetic Progression: '))
c = 1
while c < 11:
    print(f'The {c}th term of Arithmetic Progression is {term}')
    term += reason
    c += 1