from random import randint
quantidadejogos = int(input('Quantos jogos você deseja fazer?  '))
palpites = list()
aux = 0
for c in range(0, quantidadejogos):
    palpites.append([])
    for jogo in range(0, 6):
        aux = randint(1, 60)
        while aux in palpites[c]:
            aux = randint(1, 60)
        palpites[c].append(aux)
        palpites[c].sort()
    print(f'Jogo {c + 1}: {palpites[c]}')
