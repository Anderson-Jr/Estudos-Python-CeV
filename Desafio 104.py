def leiaInt(numero):
    while True:
        if numero.isnumeric():
            return numero
            break
        else:
            print('\033[31mERRO! Digite um número válido!!!\033[m')
            numero = input('Digite um número: ')


#Programa principal
n = leiaInt(input('Digite um número: '))
print(f'Você acabou de digitar o número {n}')