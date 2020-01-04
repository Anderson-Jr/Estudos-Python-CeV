perfil = dict()
perfil['Nome'] = str(input('Nome do aluno: '))
perfil['Média'] = float(input(f'Média de {perfil["Nome"]}: '))
if perfil['Média'] < 5:
    perfil['Situação'] = 'Reprovado'
elif perfil['Média'] < 7:
    perfil['Situação'] = 'Recuperação'
else:
    perfil['Situação'] = 'Aprovado'
for k, v in perfil.items():
    print(f'{k} é igual a {v}')