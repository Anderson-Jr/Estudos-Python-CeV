produtos = ('Sabão', 1.9, 'Creme Dental', 5, 'Desodorante', 12,
            'Perfume', 56.45, 'Farinha', 3.6, 'Trigo', 2.1,
            'Bolacha', 2.20, 'Arroz', 3)
print('{:=^41}'.format(' Listagem de preços '))
for c in range(0, len(produtos), 2):
    print(f'{produtos[c]:.<30}R${produtos[c + 1]:>6.2f}') # :>8.2f Serve para escrever com recuo de 6 espaços e usar apenas 2 números após a vírgula