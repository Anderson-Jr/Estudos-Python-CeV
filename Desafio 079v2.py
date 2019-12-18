valores = list()
while True:
    vt = int(input('Insira uma valor: '))
    if vt in valores:
        print('Entrada inválida. O valor já existe na lista!')
    else:
        valores.append(vt)
        laco = input('Deseja continuar? [S/N]\n')
        if laco.lower() == 'n':
            break
valores.sort()
print('Valores em ordem crescente: ', valores)