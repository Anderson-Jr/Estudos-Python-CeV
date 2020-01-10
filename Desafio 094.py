pessoas = list()
mulheres = list()
acimamedia = list()
cont = 'S'
somaidade = idadeacima = 0
while cont == 'S':
    print('REGISTRANDO PESSOAS')
    dados = {'nome': input('Nome: '), 'sexo': input('Sexo [M/F]: ').upper(), 'idade': int(input('Idade: '))}
    somaidade += dados['idade']
    if dados['sexo'] == 'F':
        mulheres.append(dados['nome'])
    pessoas.append(dados.copy())
    dados.clear()
    cont = input('Deseja continuar? [S/N]\n').upper()
print('-=' * 30)
print('Pessoas cadastradas: ', len(pessoas))
print('A média de idade foi: {:.2f}'.format(somaidade/len(pessoas)))
print('As mulheres registradas foram: ', end='')
for mulher in mulheres:
    print(mulher, end=' ')
print()
for pessoa in pessoas:
    if pessoa['idade'] > somaidade/len(pessoas):
        acimamedia.append(pessoa.copy())
        pessoa.clear()
print('As pessoas acima da média de idade foram: ')
for pessoa in acimamedia:
    for k, v in pessoa.items():
        print(f'{k} = {v}; ', end='')
    print()