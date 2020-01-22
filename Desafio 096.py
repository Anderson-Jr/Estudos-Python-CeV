def area(l, a):
    print(f'A área de um terreno {a:.2f}x{l:.2f} é {a * l:.2f}m²')


#Programa principal
print('=' * 22)
print(' Controle de Terrenos')
print('=' * 22)
altura = float(input('Insira a altura do terreno (m): '))
largura = float(input('Insira a largura do terreno(m): '))
area(altura, largura)
