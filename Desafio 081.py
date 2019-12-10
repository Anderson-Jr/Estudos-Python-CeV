numeros = list()
q = 0
while True:
    continuar = ''
    n = int(input('Insira um número inteiro: '))
    if q == 0:
        maior = menor = n
    q += 1
    numeros.append(n)
    while continuar != 'S' and continuar != 'N':
        continuar = input('Deseja continuar? [S/N]\n').strip().upper()
    if continuar == 'N':
        break
print(f'Quantidade de números digitados: {q}')
numeros.sort()
reverso = numeros[-1::-1]
print(f'Lista dos valores em ordem decrescente: {reverso}')
q = 0
if 5 in numeros:
    for num in numeros:
        if num == 5:
            q += 1
    print(f'O número 5 apareceu {q} vezes')
else:
    print('O número 5 não foi digitado!')