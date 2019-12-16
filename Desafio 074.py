from random import randint
maior = menor = n1 = randint(0, 20)
n2 = randint(0, 20)
n3 = randint(0, 20)
n4 = randint(0, 20)
n5 = randint(0, 20)
numeros = (n1, n2, n3, n4, n5)
print(numeros)
for numero in numeros:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print(f'Maior número sorteado: {maior}')
print(f'Menor número sorteado: {menor}')