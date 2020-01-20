s = cont = 0
for c in range(0, 5):
    n = int(input('Enter a integer number: '))
    if n % 2 == 0:
        s += n
        cont += 1
print(f'Numbers of even numbers: {cont}')
print(f'The sum of the numbers: {s}')
