dividers = 0
n = int(input('Enter a integer number: '))
print('The number is divisible by: ', end='')
for c in range(1, n + 1):
    if n % c == 0:
        print(f'\033[31m{c}\033[m', end=' ')
    else:
        print(c, end=' ')
