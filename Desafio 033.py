import pygame
pygame.mixer.init()
pygame.mixer.music.load('TheFatRat-unity.mp3')
pygame.mixer.music.play()
n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
n3 = int(input('Insira mais um número: '))
maior = n1
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3
if n2 > maior:
    maior = n2
elif n3 > maior:
    maior = n3
print(f'{maior} é o maior número!')
print(f'{menor} é o menor número!')

