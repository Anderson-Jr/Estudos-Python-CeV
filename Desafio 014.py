print('{:=^40}'.format(' Conversor de Temperatura '))
c = float(input('Insira a temperatura em Celsius: '))
f = (c * 9) / 5 + 32
print('{} celsius equivalem a {:.2f} fahrenheit!'.format(c, f))
