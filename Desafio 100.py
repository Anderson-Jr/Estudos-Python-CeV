from random import randint
def sorteia():
    for c in range (0, 5):
        numeros.append(randint(0, 10))
        c += 1

def somapar():
    sp = 0
    for v in numeros:
        if v % 2 == 0:
            sp += v
    print('Soma dos pares: ', sp)

#Programa principal
numeros = list()
sorteia()
print(numeros)
somapar()
