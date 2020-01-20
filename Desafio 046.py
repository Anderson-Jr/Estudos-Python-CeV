from time import sleep
for c in range(10, -1, -1):
    print(c, "...", end='')
    sleep(1)
print('\nEnd of count!')