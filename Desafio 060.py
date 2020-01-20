f = 1
n = int(input('Enter a integer number: '))
while n > 0:
    if n > 1:
        print(f'{n} x ', end='')
    else:
        print(f'1 = {f}')
    n -= 1
    f *= n