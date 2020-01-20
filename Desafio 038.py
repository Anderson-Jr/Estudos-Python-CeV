n1 = int(input('Enter a integer number: '))
n2 = int(input('Enter another integer number: '))
if n1 > n2:
    print(f'{n1} é o maior valor')
elif n2 > n1:
    print(f'{n2} é o maior valor')
else:
    print('Não existe valor maior, os números são iguais!')