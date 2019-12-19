valores = list()
for c in range(0, 5):
    vt = int(input('Insira um número: '))
    if c == 0:
        valores.append(vt)
    else:
        for pos, numero in enumerate(valores):
            if vt <= numero:
                valores.insert(pos, vt)
                print(f'Número {vt} adicionado na posição {pos}')
                break
            elif vt > valores[len(valores)-1]:
                valores.append(vt)
                print(f'Número {vt} adicionado na última posição')
                break
print(f'Valores inseridos {valores}')