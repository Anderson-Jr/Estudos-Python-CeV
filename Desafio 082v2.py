todos = list()
pares = list()
impares = list()
for c in range(0, 5):
	todos.append(int(input('Insira um número: ')))
for numero in todos:
	if numero % 2 == 0:
		pares.append(numero)
	else:
		impares.append(numero)
print('Lista completa: ', todos)
print('Números pares: ', pares)
print('Números ímpares: ', impares)