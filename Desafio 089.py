alunosenotas = list()
cont = 's'
c = 0
while cont.lower() == 's':
    alunosenotas.append([])
    print('{:*^30}'.format(' Novo aluno '))
    alunosenotas[c].append(input('Insira o nome do aluno: '))
    print('{:=^30}'.format(alunosenotas[c][0]))
    alunosenotas[c].append(float(input(f'Insira a primeira nota: ')))
    alunosenotas[c].append(float(input(f'Insira a segunda nota: ')))
    cont = input('Deseja continuar? [S/N]\n')
    c += 1
print('=' * 30)
print('{:<5}{:<12}{:<4}'.format('No.', 'NOME', 'MÉDIA'))
for pos, aluno in enumerate(alunosenotas):
    media = (alunosenotas[pos][1] + alunosenotas[pos][2])/2
    print(f'{pos:<5}{alunosenotas[pos][0]:<12}{media:<4.2f}')
while True:
    print('-' * 30)
    alunoescolhido = int(input('Mostrar notas de qual aluno? (999 para interromper): '))
    if alunoescolhido == 999:
        break
    print(f'As notas de {alunosenotas[alunoescolhido][0]} são: {alunosenotas[alunoescolhido][1:3]}')
    print('-' * 30)
print('Finalizando...')