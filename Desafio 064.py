n = sm = count = 0
print('Enter 999 to exit!')
while n != 999:
    n = int(input('Enter a number: '))
    sm += n
    count += 1
sm -= 999
count -= 1
print(f'The plus: {sm}')
print(f'Count: {count}')
