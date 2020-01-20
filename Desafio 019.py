from random import choice
a = input('Enter the first name: ')
b = input('Enter the second name: ')
c = input('Enter the third name: ')
d = input('Enter the fourth name: ')
students = [a, b, c, d]
print('The winner student is {}!'.format(choice(students)))
