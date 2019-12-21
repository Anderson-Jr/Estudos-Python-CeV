todos = [[], []]
p = i = 0
for c in range(1, 8):
    aux = (int(input(f'Digite o {c}o valor: ')))
    if aux % 2 == 0:
        todos[0].append(aux)
    else:
        todos[1].append(aux)
todos.sort()
print(todos)
print('Números ímpares: ', todos[1])
print('Números pares: ', todos[0])