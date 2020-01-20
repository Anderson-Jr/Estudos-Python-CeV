from datetime import date
atual = date.today().year
nasc = int(input('What is the year of your birth?\n '))
age = atual - nasc
if age == 18:
    print('You have to join the army!')
elif age < 18:
    print(f'{18 - age} years to join the army!')
else:
    print(f'{age - 18} years later of join the army!')
