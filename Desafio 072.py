numeros = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte']
escolha = int(input('Insira um número inteiro entre 0 e 20: '))
while True:
    if escolha < 0 or escolha > 20:
        print('Valor inválido!')
        escolha = int(input('Insira um número inteiro entre 0 e 20: '))
    else:
        break
print(numeros[escolha])
