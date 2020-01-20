from emoji import emojize
distancia = float(input(emojize('Qual a distância que será percorrida em km/h? :smiley:\n', use_aliases=True)))
if distancia <= 200:
    passagem = distancia * 0.5
else:
    passagem = distancia * 0.45
print(emojize(f'O preço da sua passagem é R${passagem:.2f} :dollar:! Aproveite a viagem! :minibus:', use_aliases=True))
