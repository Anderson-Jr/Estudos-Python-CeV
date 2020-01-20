average = sm = count = 0
confirm = 'Y'
while confirm == 'Y':
    n = int(input('Enter a integer number: '))
    if count == 0:
        maxn = minn = n
    sm += n
    confirm = input('Do you want to continue? [Y/N]\n').strip().upper()
    count += 1
    if n > maxn:
        maxn = n
    if n < minn:
        minn = n
average = sm/count
print(f'The average is {average:.2f}')
print(f'The max: {maxn}')
print(f'The min: {minn}')
