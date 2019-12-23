matriz = [[], [], []]
sp = stc = mvsl= 0
for l in range (0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Insira um valor para a posição [{l}, {c}]: ')))
for l in range (0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            sp += matriz[l][c]
        if c == 2:
            stc += matriz[l][2]
        if (l == 1) and (c == 0):
            mvsl = matriz[1][0]
        if (l == 1) and (matriz[1][c] > mvsl):
            mvsl = matriz[1][c]
        print(f'[  {matriz[l][c]}  ]', end='')
    print('')
print(f'A soma dos valores pares é: {sp}')
print(f'A soma dos valores da terceira coluna é: {stc}')
print(f'O maior valor da segunda linha é: {mvsl}')