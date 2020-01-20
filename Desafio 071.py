valor = int(input('Qual o valor a ser sacado?\n'))
if valor // 50 > 0:
    cedulas = valor // 50
    print(f'Cédulas de R$50,00: {cedulas}')
    valor = valor % 50
if valor // 20 > 0:
    cedulas = valor // 20
    print(f'Cédulas de R$20,00: {cedulas}')
    valor = valor % 20
if valor // 10 > 0:
    cedulas = valor // 10
    print(f'Cédulas de R$10,00: {cedulas}')
    valor = valor % 10
if valor // 5 > 0:
    cedulas = valor // 5
    print(f'Cédulas de R$5,00: {cedulas}')
    valor = valor % 5
if valor // 2 > 0:
    cedulas = valor // 2
    print(f'Cédulas de R$2,00: {cedulas}')
    valor = valor % 2
if valor // 1 > 0:
    cedulas = valor // 1
print(f'Cédulas de R$1,00: {cedulas}')
