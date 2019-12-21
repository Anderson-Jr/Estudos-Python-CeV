dados = list()
aux = list()
conf = 's'
qt = menorp = maiorp = 0
while conf.lower() == 's':
    aux.append(input('Insira o nome da pessoa: '))
    aux.append(int(input('Insira o peso da pessoa: ')))
    if qt == 0:
        menorp = maiorp = aux[-1]
    if aux[-1] < menorp:
        menorp = aux[-1]
    if aux[-1] > maiorp:
        maiorp = aux[-1]
    dados.append(aux[:])
    aux.clear()
    qt += 1
    conf = input('Deseja continuar? [S/N]')
print('Quantidade de pessoas cadastradas: ', qt)
print('A pessoa mais pesada registrada foi: ', maiorp)
print('A pessoa mais leve registrada foi: ', menorp)