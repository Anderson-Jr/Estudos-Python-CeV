n = int(input('Enter a term to see in the Fibonacci sequence: '))
c = 0
v1 = v3 = 0
v2 = 1
while c < n:
    c += 1
    print(v3)
    v1 = v2
    v2 = v3
    v3 = v1 + v2
