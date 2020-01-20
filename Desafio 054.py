from datetime import date
current = date.today().year
plus18 = minus18 = 0
for c in range(0, 7):
    birth = int(input('Enter the year of your birth: '))
    age = current - birth
    if age >= 18:
        plus18 += 1
    else:
        minus18 += 1
print(f'The number of people over 18 years old is: {plus18}')
print(f'The number of people under 18 years old is: {minus18}')
