import pygame
pygame.mixer.init()
pygame.mixer.music.load('supermarioworld.mp3')
pygame.mixer.music.play()
nome = input('Insira seu nome completo: ').strip().split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
