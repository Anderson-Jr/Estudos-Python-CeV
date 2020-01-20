for c in range(1, 6):
    weight = float(input(f'Weight {c}: '))
    if c == 1:
        max = min = weight
    if weight > max:
        max = weight
    elif weight < min:
        min = weight
print(f'The max weight registered is {max}')
print(f'The min weight registered is {min}')
