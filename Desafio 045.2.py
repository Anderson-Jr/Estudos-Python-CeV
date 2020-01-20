from random import randint
import pygame
from time import sleep
option = ['Rock', 'Paper', 'Scissor']
pygame.mixer.init()
pygame.mixer.music.load('panic.mp3')
pygame.mixer.music.play()
name = input('What is your name?\n')
pygame.mixer.music.load('game.mp3')
pygame.mixer.music.play()
sleep(4)
computer = player = 0
while not(computer == 0 and player == 1 or player == 1 and computer == 3 or player == 2 and computer == 0):
    computer = randint(0, 2)
    print('=' * 40)
    print('{:^40}'.format(' JO KEN PO '))
    print('=' * 40)
    print('[0] Rock \n[1] Paper \n[2] Scissor')
    player = int(input('Make your choice: '))
    print('=' * 40)
    print(f'Computer chose {option[computer]}')
    print(f'Player chose {option[player]}')
    print('=' * 40)
    if computer == player:
        print('The game was a draw!')
    elif computer == 0 and player == 1 or player == 1 and computer == 3 or player == 2 and computer == 0:
        print('The computer is the winner!')
        sleep(1)
        pygame.mixer.music.load('gameover2.mp3')
        pygame.mixer.music.play()
        sleep(3)
    else:
        print('You are the winner!!!')
        sleep(1)
        pygame.mixer.music.load('alive.mp3')
        pygame.mixer.music.play()
        sleep(5)
        print('=' * 40)
        print('============= PLAY AGAIN ==============')
