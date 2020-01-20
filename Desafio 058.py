count = 1
from random import randint
player = int(input('Enter a integer number between 0 and 10: '))
computer = randint(0, 10)
while player != computer:
    print('You lost!')
    player = int(input('Enter another integer number: '))
    count += 1
print(f'You won after {count} times')
