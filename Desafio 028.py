from random import randint
computador = randint(0, 5)
jogador = int(input('Escolha um número: '))
if jogador == computador:
    print('Você venceu!')
else:
    print('Você perdeu!!')
    print(f'Computador escolheu: {computador}')
