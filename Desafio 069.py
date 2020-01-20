mais18 = homens = menos20 = pessoas = 0
c = 1
while True:
    print(f'----------- {c} PESSOA -------------')
    pessoas += 1
    idade = int(input('Idade: '))
    opcao = sexo = ''
    while True:
        if sexo == 'F' or sexo == 'M':
            break
        else:
            sexo = str(input('Sexo [M/F]: ')).strip().upper()
    while True:
        if opcao == 'S' or opcao == 'N':
            break
        else:
            opcao = str(input('Deseja continuar? [S/N] \n')).strip().upper()
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        menos20 += 1
    if opcao == 'N':
        break
print(f'Pessoas maiores de 18 anos: {mais18}')
print(f'Homens cadastrados: {homens}')
print(f'Mulheres com menos de 20 anos: {menos20}')
print(f'Pessoas registradas: {pessoas}')
