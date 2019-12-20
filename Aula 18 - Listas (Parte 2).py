dados = list()
dados.append('Pedro')
dados.append(25)
dados.append('Maria')
dados.append(28)
dados.append('Cássio')
dados.append(90)
print(dados[0])
print(dados[1])
pessoas = list()
pessoas.append(dados[:])
print(pessoas[0])
pessoas.append(dados[:])
print(pessoas)
del pessoas
pessoas = [['Pedro', 25], ['Maria', 28], ['João', 90]]
print(pessoas)
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
#galera.append(teste) # Cria uma ligação permanente entre as duas listas
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
del galera
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0][0])
for pessoa in galera:
    print(f'Nome: {pessoa[0]}\nIdade: {pessoa[1]}')
dado = list()
print('Adicionando mais pessoas na lista...')
for c in range(0, 3):
    dado.append(input('Insira um nome: '))
    dado.append(int(input('Insira a idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
print('Mostrando apenas pessoas acima de 20 anos: ')
tmenor = tmaior = 0
for pessoa in galera:
    if pessoa[1] > 20:
        print(pessoa)
        tmaior += 1
    else:
        tmenor += 1
print('Maiores de idade: ', tmaior)
print('Menores de idade: ', tmenor)