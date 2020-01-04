jogador = {'nome': input('Nome do jogador: '),
           'partidas': int(input('Partidas jogadas: '))}
jogador['totalgols'] = 0
golspartida = list()
for c in range(0, jogador['partidas']):
    golspartida.append(int(input(f'Gols feitos na partida {c + 1}: ')))
    jogador['totalgols'] += golspartida[c]
jogador['gols por partida'] = golspartida.copy()
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas')
for p, g in enumerate(golspartida):
    print(f'      => Na partida {p + 1}, {jogador["nome"]} fez {g} gols')
print(f'Foi um total de {jogador["totalgols"]} gols')