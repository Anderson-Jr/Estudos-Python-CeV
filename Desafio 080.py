numeros = list()
for c in range(0, 5):
    n = int(input('Enter a integer number: '))
    if c == 0 or n > numeros[-1]:
        numeros.append(n)
        print('Adicionado ao final da lista!')
    else:
        pos = 0            #Posição de leitura
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print(f"Os valores digitados foram: {numeros}")