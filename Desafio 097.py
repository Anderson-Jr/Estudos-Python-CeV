def escrever(mensagem):
    print('~' * (len(mensagem) + 2))
    print(f' {mensagem}')
    print('~' * (len(mensagem) + 2))


#Programa principal
for c in range(0, 3):
    msg = input('Insira um texto: ')
    escrever(msg)
