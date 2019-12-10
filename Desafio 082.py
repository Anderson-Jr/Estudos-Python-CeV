numeros = list()
pares = list()
impares = list()
q = 0
while True:
    continuar = ''
    n = int(input('Insira um número inteiro: '))
    q += 1
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    while continuar != 'S' and continuar != 'N':
        continuar = input('Deseja continuar? [S/N]\n').strip().upper()
    if continuar == 'N':
        break
print(f'Quantidade de números digitados: {q}')
print(f'Lista completa: {numeros}')
print(f'Números ímpares: {impares}')
print(f'Números pares: {pares}')
