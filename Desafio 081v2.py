valores = list()
cont = 0
conf = 's'
while conf.lower() == 's':
		valores.append(int(input('Insira um valor: ')))
		conf = input('Deseja continuar? [S/N]')
		cont += 1
valores.sort(reverse=True)
print('Lista em ordem descrescente', valores)
print('quantidade de valores', cont)
if 5 in valores:
	print('O valor 5 foi encontrado na lista')
else:
	print('O valor 5 não foi encontrado')