matriz = [[], [], []]
for l in range (0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Insira um valor para a posição [{l}, {c}]: ')))
for l in range (0, 3):
    for c in range(0, 3):
        print(f'[  {matriz[l][c]}  ]', end='')
    print('')