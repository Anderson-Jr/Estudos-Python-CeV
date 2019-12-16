times = ['Santos', 'Flamengo', 'Palmeiras', 'Atlético - MG', 'São Paulo', 'Corinthians', 'Internacional', 'Athletico - PR', 'Botafogo', 'Bahia', 'Ceará', 'Goiás', 'Grêmio', 'Fortaleza', 'Vasco da Gama', 'Cruzeiro', 'Chapecoense', 'Fluminense', 'CSA', 'Avaí']
print('Cinco primeiros colocados: ', times[:4])
print('Últimos 4 colocados: ', times[-4:])
org = sorted(times)
print('Times em ordem alfabética: ', org)
for pos, time in enumerate(times):
    if time == 'Palmeiras':
        print('Colocação do Palmeiras: ', pos + 1)