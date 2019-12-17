valores = (int(input('Insira um valor: ')), int(input('Insira outro valor: ')), int(input('Insira mais um valor: ')), int(input('Insira o último valor: ')))
print('Incidência do número 9:', valores.count(9))
if 3 in valores:
    print('O primeiro valor 3 foi digitado na posição:', valores.index(3) + 1)
else:
    print('O valor 3 não foi digitado!')
print('Os números pares foram: ', end = '')
for numero in valores:
    if numero % 2 == 0:
        print(numero, end = ' ')