from uteis import numeros
preco = float(input('Digite o preço: '))
print(f'A metade de R${preco} é R${numeros.metade(preco):.2f}')
print(f'O dobro de R${preco} é R${numeros.dobro(preco)}')
porcentagem = float(input('Porcentagem de aumento: '))
print(f'Aumetando {porcentagem}, temos R${numeros.aumento18(preco, porcentagem)}')