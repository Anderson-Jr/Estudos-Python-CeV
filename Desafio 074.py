from random import randint
a = randint(0, 10)
b = randint(0, 10)
c = randint(0, 10)
d = randint(0, 10)
e = randint(0, 10)
numeros = [a, b, c, d, e]
print(a, b, c, d, e)
for pos, numero in enumerate(numeros):
    print(f'Posição: {pos}')
    print(f'Número: {numero}')
    if pos == 0:
        menor = maior = numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print('Maior número: ', maior)
print('Menor número: ', menor)
