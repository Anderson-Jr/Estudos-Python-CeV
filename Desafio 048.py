s = cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print(f'The sum is {s}')
print(f'The number of numbers has been {cont}')