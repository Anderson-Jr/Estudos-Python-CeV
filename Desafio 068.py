from random import randint
victory = 0
while True:
    computer = randint(0, 10)
    player = int(input('Enter a integer number: '))
    sm = computer + player
    option = int(input('Choose between [1] Pair or [2] Odd: '))
    print(computer)
    if sm % 2 == 0:
        result = 1
    else:
        result = 2
    if result != option:
        break
    else:
        victory += 1
print(f'Consecutive wins: {victory}')
