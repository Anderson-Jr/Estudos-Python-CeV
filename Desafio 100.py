from random import randint
from time import sleep
def sorteia():
    print('Sorteando os 5 valores: ', end='')
    for c in range(0, 5):
        sleep(0.3)
        valor = randint(0, 10)
        numeros.append(valor)
        print(valor, end=' ')
        c += 1
    print('PRONTO!')

def somapar():
    sp = 0   
    for v in numeros:
        if v % 2 == 0:
            sp += v
    print('Soma dos pares: ', sp)  

#Programa principal
numeros = list()
sorteia()
somapar()