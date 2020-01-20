n = sm = count = 0
print('Enter 999 to exit!')
while True:
    n = int(input('Enter a number: '))
    if n != 999:
        sm += n
        count += 1
    else:
        break
print(f'The plus: {sm}')
print(f'Count: {count}')
