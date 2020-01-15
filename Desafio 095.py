cont = 'S'
golspartida = list()
jogadores = list()
while cont == 'S':
    jogador = {'nome': input('Nome do jogador: '),
               'partidas': int(input('Partidas jogadas: '))}
    jogador['totalgols'] = 0
    for c in range(0, jogador['partidas']):
        golspartida.append(int(input(f'Gols feitos na partida {c + 1}: ')))
        jogador['totalgols'] += golspartida[c]
    jogador['gols por partida'] = golspartida.copy()
    golspartida.clear()
    jogadores.append(jogador.copy())
    jogador.clear()
    cont = input('Deseja continuar? [S/N]').upper()
print('-=' * 30)
for jogador in jogadores:
    for k, v in jogador.items():
        print(f'O campo {k} tem o valor {v}')
    print('-=' * 30)
    print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas')
    for p, g in enumerate(jogador['gols por partida']):
        print(f'      => Na partida {p + 1}, {jogador["nome"]} fez {g} gols')
    print(f'Foi um total de {jogador["totalgols"]} gols')
    print('-=' * 30)