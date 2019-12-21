todos = list()
pares = list()
impares = list()
for c in range (1, 8):
    aux = (int(input(f'Digite o {c}o valor: ')))
    todos.append(aux)
    if aux % 2 == 0:
        pares.append(aux)
    else:
        impares.append(aux)
pares.sort()
impares.sort()
todos.sort()
print(todos)
print('Números ímpares: ', impares)
print('Números pares: ', pares)