nome = input('Digite o nome da sua cidade: ').upper()
nome = nome.strip().split()
print('Possui "Santo" no primeiro nome?', 'SANTO' in nome[0])
