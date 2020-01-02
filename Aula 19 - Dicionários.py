dados = dict()
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M'
print(dados)
del dados['idade']
print(dados)
print('-'*40)
filme1 = {'título': 'Star Wars',
'ano': 1977,
'diretor': 'George Lucas'
}
print(filme1.values())
print(filme1.keys())
print(filme1.items())
for k, v in filme1.items():
    print(f'O {k} é {v}')
locadora = list() #vai guardar as informações de vários filmes
locadora.append(filme1)
filme2 = {'título': 'The Avengers',
          'ano': 2012,
          'diretor': 'Joss Whedon'
}
filme3 = {'título': 'Matrix',
          'ano': 2012,
          'diretor': 'Wachowski'

}
locadora.append(filme2)
locadora.append(filme3)
for c in range(0, 3):
    print(f'O filme {locadora[c]["título"]} foi lançado em {locadora[c]["ano"]} pelo diretor {locadora[c]["diretor"]}')
print('-'*40)
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
for i in pessoas.items():
    print(i)
for k, v in pessoas.items():
    print(f'{k} = {v}')
del pessoas['sexo']
print(pessoas)
pessoas['nome'] = 'Leandro'
print(pessoas)
pessoas['peso'] = 98.5
print(pessoas)
print('-'*40)
brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])
print('-'*40)
estados = dict()
brasils = list()
for c in range(0, 3):
    estados['uf'] = input('Unidade Federativa: ')
    estados['sigla'] = input('Sigla do Estado: ')
    brasils.append(estados.copy()) #Copiar o conteúdo de um dicionário
print(brasils)
for estado in brasils:
    for k, v in estado.items():
        print(f'O campo {k} tem valor {v}')
print('-'*40)
for e in brasils:
    for v in e.values():
        print(v, end=' ')
    print()
