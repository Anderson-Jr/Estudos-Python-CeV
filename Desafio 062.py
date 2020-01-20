term = int(input('Enter the first term: '))
reason = int(input('Enter the reason of Arithmetic Progression: '))
c = 1
total = more = 11
while more != 0:
    while c < total:
        print(f'The {c}th term of Arithmetic Progression is {term}')
        term += reason
        c += 1
    more = int(input('Do you want to see more terms? How many?\n'))
    total += more