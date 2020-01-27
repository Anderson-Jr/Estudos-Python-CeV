def maior(lista):
    maior = lista[0]
    for v in lista:
        if v > maior:
            maior = v
    print(f'Ao todo foram passados {tot} valores')
    print(f'O maior valor registrado foi {maior}')


#Programa principal
lista = list()
tot = 0
while True:
    lista.append(int(input('Insira um valor: ')))
    tot += 1
    cont = input('Deseja continuar? [S/N]').upper()
    if cont[0] == 'N':
        break
maior(lista)
