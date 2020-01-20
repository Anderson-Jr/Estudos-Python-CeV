from emoji import emojize
a = float(input('Insira o valor do primeiro lado do triângulo: '))
b = float(input('Insira o valor do segundo lado do triângulo: '))
c = float(input('Insira o valor do terceiro lado do triângulo: '))
if a + b > c and a + c > b and b + c > a:
    print(emojize('É um triângulo possível! :small_red_triangle:', use_aliases=True))
else:
    print('Não é um triângulo possível!')
