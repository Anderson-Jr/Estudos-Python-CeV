times = ['Santos', 'Flamengo', 'Palmeiras', 'Atlético - MG', 'São Paulo', 'Corinthians', 'Internacional', 'Athletico - PR', 'Botafogo', 'Bahia', 'Ceará', 'Goiás', 'Grêmio', 'Fortaleza', 'Vasco da Gama', 'Cruzeiro', 'Chapecoense', 'Fluminense', 'CSA', 'Avaí']
print('Cinco primeiros colocados: ', times[0:4])
print('Últimos 4 colocados: ', times[-4:])
org = sorted(times)
print('Times em ordem alfabética: ', org)
print('Colocação do Palmeiras: ', times.index('Palmeiras')+1)
