from math import hypot
a = float(input('Insira o valor do cateto oposto: '))
b = float(input('Insira o valor de cateto adjascente: '))
c = hypot(a, b)
print('O valor da hipotenusa é {:.2f}'.format(c))
