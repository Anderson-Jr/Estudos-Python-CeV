from time import sleep
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    if (inicio > fim):
        print(f'Contando de {inicio} até {fim} de {passo} em {passo}')
        passo *= -1
        for c in range(inicio, fim - 1, passo):
            print(c, end='... ')
    else:
        print(f'Contando de {inicio} até {fim} de {passo} em {passo}')
        for c in range(inicio, fim + 1, passo):
            print(c, end='... ')
    print()


#Programa principal
print('-=' * 12)
print('Contando de 1 até 10 de 1 em 1:')
for c in range(1, 11, 1):
    print(c, end='... ')
print()
print('=-' * 12)
print('Contando de 10 até 0 de 2 em 2:')
for c in range(10, 0, -2):
    print(c, end='... ')
print()
print('=-' * 13)
print('  Contagem personalizada')
print('-=' * 13)
contador(int(input('Início da contagem personalizada: ')),
         int(input('Término da contagem personalizada: ')),
         int(input('Salto da contagem: ')))
