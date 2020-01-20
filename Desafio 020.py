from random import shuffle
a = input('Digite o primeiro nome: ')
b = input('Digite o segundo nome: ')
c = input('Digite o terceiro nome: ')
d = input('Digite o quarto nome: ')
students = [a, b, c, d]
shuffle(students)
print('A ordem de estudantes sorteados é {}'.format(students))
