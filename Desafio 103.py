def validar(nome, gols):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')

#Programa principal
name = str(input('Nome do jogador: '))
ngols = str(input('Número de gols: '))
if ngols.isnumeric():
    ngols = int(ngols)
else:
    ngols = 0
if len(name.strip()) == 0:
    name = '<desconhecido>'
validar(name, ngols)
