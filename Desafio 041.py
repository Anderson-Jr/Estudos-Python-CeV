from datetime import date
current = date.today().year
birth = int(input('Enter your birth day: '))
age = current - birth
if age < 9:
    category = 'Mirim'
elif age < 14:
    category = 'Infantil'
elif age < 19:
    category = 'Junior'
elif age < 20:
    category = 'Sênior'
else:
    category = 'Master'
print(f'The athlete category is {category}')
