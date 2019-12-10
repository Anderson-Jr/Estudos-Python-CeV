numeros = list()
n = 0
while True:
    opcao = ''
    n = int(input('Enter a number: '))
    if n in numeros:
        print('O número já existe na lista')
    else:
        numeros.append(n)
    while opcao != 'S' and opcao != 'N':
        opcao = input('Do you want to continue? [S/N]\n').upper().strip()
    if opcao == 'N':
        break
numeros.sort()
print(f'Números digitados: {numeros}')
