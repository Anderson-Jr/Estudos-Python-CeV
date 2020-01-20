import pygame
from emoji import emojize
pygame.mixer.init()
pygame.mixer.music.load('spinnings-monkeys.mp3')
pygame.mixer.music.play()
salario = float(input(emojize('Insira o seu salário em reais :dollar::dollar::dollar: R$', use_aliases=True)))
if salario > 1250:
    aumento = salario * 1.1
else:
    aumento = salario * 1.15
print('Seu novo salário é R${:.2f}'.format(aumento))
