average = countf = sm = count20 = age = agemax = 0
for c in range(1, 5):
    print('------- PERSON {} -------'.format(c))
    name = input('What is your name? \n').strip()
    age = int(input('How old are you? \n'))
    sex = input('What is your sexuality? \n').strip().upper()
    sm += age
    if sex == 'F' and age < 20:
        count20 += 1
    if sex == 'M' and age > agemax:
        agemax = age
        namemax = name
average = sm / 4
print(f'The average age is: {average:.2f}')
print(f'The men most old is {agemax} and his name is {namemax}')
print(f'{count20} women has under 20 years old')
