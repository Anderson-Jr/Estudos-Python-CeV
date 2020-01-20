while True:
    n = int(input('Enter a integer number: '))
    c = 1
    if n >= 0:
        while c < 11:
            print(f'{c} x {n} = {c * n}')
            c += 1
    else:
        break
