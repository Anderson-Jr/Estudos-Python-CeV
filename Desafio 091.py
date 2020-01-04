from random import randint
from time import sleep
from operator import itemgetter
resultados = {'jogador1': randint(1, 6),
              'jogador2': randint(1, 6),
              'jogador3': randint(1, 6),
              'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados: ')
for k, v in resultados.items():
    print(f'O {k} tirou {v}')
    sleep(1)
ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
print('-=' *30)
print('        == RANKING DO JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'  O {i+1}º lugar foi {v[0]} que ficou com {v[1]}')