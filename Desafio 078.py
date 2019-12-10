posmaior = posmenor = 0
numeros = list()
for c in range(0, 4):
    numeros.append(int(input('Enter a integer number: ')))
    if c == 0:
        maior = menor = numeros[c]
    if numeros[c] > maior:
        maior = numeros[c]
        posmaior = c
    if numeros[c] < menor:
        menor = numeros[c]
        posmenor = c
print(f'Maior número está na posição: {posmaior}')
print(f'Menor número está na posição: {posmenor}')