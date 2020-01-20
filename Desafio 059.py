v1 = int(input('Enter a integer number: '))
v2 = int(input('Enter another integer number: '))
option = 0
while option != 5:
    option = int(input('[1] Plus \n[2] Multiply \n[3] The max \n[4] New numbers [5] Exit \nMake your choice: '))
    if option == 1:
        print(f'{v1} + {v2} = {v1 + v2}')
    if option == 2:
        print(f'{v1} x {v2} = {v1 * v2}')
    if option == 3:
        if v1 > v2:
            print(f"{v1} is the biggest")
        elif v2 > v1:
            print(f'{v2} is the biggest')
        else:
            print(f'Numbers are the same')
    if option == 4:
        v1 = int(input('Enter a new number: '))
        v2 = int(input('Enter another new number: '))
    print('========================================')
