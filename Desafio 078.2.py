numeros = list()
for c in range(0, 4):
    numeros.append(int(input('Enter a integer number: ')))
    if c == 0:
        maior = menor = numeros[c]
    if numeros[c] > maior:
        maior = numeros[c]
    if numeros[c] < menor:
        menor = numeros[c]
print('Maior número está na posição: ', end='')
for pos, numero in enumerate(numeros):
    if numero == maior:
        print(pos, end=' ')
print('Menor número está na posição: ', end='')
for pos, numero in enumerate(numeros):
    if numero == menor:
        print(pos, end=' ')