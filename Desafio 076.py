print('{:=^50}'.format(' Listagem de produtos '))
produtos = ['Máquina de lavar', 699.99, 'Bicicleta', 1789, 'Sabonete', 1.34]
c = 0
for c in range(0, len(produtos), 2):
    print(f'{produtos[c]:.<40} R${produtos[c + 1]:>7.2f}')
