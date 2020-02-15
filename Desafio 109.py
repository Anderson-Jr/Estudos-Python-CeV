from uteis import numeros
preco = float(input('Digite o preço: '))
print(f'A metade de {numeros.moeda(preco)} é {numeros.metade(preco, True)}')
print(f'O dobro de {numeros.moeda(preco)} é {numeros.dobro(preco, True)}')
porcentagem = float(input('Porcentagem de aumento: '))
print(f'Aumetando {porcentagem}%, temos {numeros.aumentar(preco, 10, True)}')