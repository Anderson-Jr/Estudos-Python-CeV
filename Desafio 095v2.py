time = list()
jogador = dict()
golspartidas = list()
while True:
    jogador['nome'] = input('Nome do jogador: ')
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    for c in range(0, tot):
        golspartidas.append(int(input(f'    Quantos gols na partida {c + 1}?')))
    jogador['gols por partida'] = golspartidas.copy()
    jogador['total'] = sum(golspartidas)
    time.append(jogador.copy())
    golspartidas.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print('-=' * 40)
print(f'{"cod":<5}{"gols":<22}{"nome":<22}{"total":<22}')
for pos, jogador in enumerate(time):
    print(f'{pos:<5}', end='')
    for dado in jogador.values():
        print(f'{str(dado):<22}', end='')
    print()
print('-=' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time) or busca < 0:
        print(f'ERRO! não existe jogador com código {busca}')
    else:
        print(f'=> Levantamento do jogador {time[busca]["nome"]}')
        for partida, numgols in enumerate(time[busca]['gols por partida']):
            print(f'    Na partida {partida + 1} o jogador marcou {numgols} gols')
    print('-' * 60)
print('<<< VOLTE SEMPRE >>>')