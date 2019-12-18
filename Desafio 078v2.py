valores = list()
for c in range(0, 5):
    valores.append(int(input('Insira um valor: ')))
    if c == 0:
        maior = menor = valores[0]
print('Você digitou os valores', valores)
for pos, numero in enumerate(valores):
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print(f'Maior número {maior} na(s) posição: ', end='')
for pos, numero in enumerate(valores):
    if numero == maior:
        print(pos, end='... ')
print(f'\nMenor número {menor} na(s) posição: ', end='')
for pos, numero in enumerate(valores):
    if numero == menor:
        print(pos, end='... ')