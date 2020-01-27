from time import sleep
def maior(*numeros):
    cont = 0
    print('\nAnalisando valores passados: ')
    if len(numeros) == 0:
        print('Nenhum valor inserido! ')
    else:
        maior = numeros[0]
        for valor in numeros:
            if valor > maior:
                maior = valor
            print(f'{valor} ', end='', flush=True)
            cont += 1
            sleep(0.3)
        print(f'Foram informados {cont} valores')
        print(f'O maior valor informado foi {maior}')


#Programa principal
maior(2, 4, 2, 4, 4, 5, 3, 2)
maior(2, 3, 2, 5, 55, 3)
maior()
maior(6, 3, 2)
maior(1, 2)
maior(9)
