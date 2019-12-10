numeros = (int(input('Enter a number: ')), int(input('Enter another number: ')), int(input('Enter another number: ')), int(input('Enter another number: ')))
print(f'You entered the values: {numeros}')
print(f'The number nine  :', numeros.count(9))
print(f'O valor 3 foi digitado nas posições: ', end=' ')
if 3 in numeros:
    print(numeros.index(3) + 1)
else:
    print('O número não foi digitado')
print('Os números pares foram: ', end=' ')
for numero in numeros:
    if numero % 2 == 0:
        print(numero)