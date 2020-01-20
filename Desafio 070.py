totalgasto = maismil = total = 0
while True:
    opcao = str()
    nome = input('Nome do produto: ')
    preco = float(input('Preço do produto: R$'))
    while True:
        if opcao == 'S' or opcao == 'N':
            break
        else:
            opcao = str(input('Deseja continuar? [S/N] \n')).strip().upper()
    if total == 0:
        menor = preco
    total += preco
    if preco < menor:
        menor = preco
        nomemenor = nome
    if preco > 1000:
        maismil += 1
    if opcao == 'N':
        break
print(f'Total gasto em compras: R${total}')
print(f'Quantidade de produtos acima de R$1000: {maismil}')
print(f'O produto mais barato foi: {nomemenor}')
