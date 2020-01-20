from math import sqrt
a = float(input('Insira um lado do triângulo: '))
b = float(input('Insira outro lado do triângulo: '))
c = sqrt(a**2+b**2)
print('A valor da hipotenusa é: {:.2f}'.format(c))
