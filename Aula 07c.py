n1 = int(input('Enter a value: '))
n2 = int(input('Input another: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1**n2
rd = n1 % n2
print('A soma vale {} \nA multiplicação vale {}, a divisão vale {:.3f}'.format(s, m, d), end=' ')
print('a divisão inteira vale {}, a exponenciação vale {}\nO resto da divisão vale {}'.format(di, e, rd))
