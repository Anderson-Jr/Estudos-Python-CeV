times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('Cinco primerios colocados: ', times[0:5])
print('Os quatro últimos colocados: ', times[-4:])
ordem = sorted(times)
print('Lista dos times em ordem alfebética: ', ordem)
for pos, time in enumerate(times):
    if time == 'Chapecoense':
        print('Chapecoense está na posição: ', pos)