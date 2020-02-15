from uteis import numeros
preco = float(input('Digite o preço: '))
print(f'A metade de {numeros.moeda(preco)} é {numeros.moeda(numeros.metade(preco))}')
print(f'O dobro de {numeros.moeda(preco)} é {numeros.moeda(numeros.dobro(preco))}')
porcentagem = float(input('Porcentagem de aumento: '))
print(f'Aumetando {porcentagem}%, temos {numeros.moeda(numeros.aumento(preco, porcentagem))}')