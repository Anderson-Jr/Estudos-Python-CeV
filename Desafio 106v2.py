from time import sleep
c = ('\033[m', # 0 - sem cores
     '\033[1;41m', # 1 - vermelho
     '\033[1;42m', # 2 - verde
     '\033[1;43m', # 3 - amarelo
     '\033[1;44m', # 4 - azul
     '\033[1;45m', # 5 - magenta
     '\033[1;46m', # 6 - cyan
     )

def ajuda(com):
    titulo(f"Acessando o manual do comando '{com}'", 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(msg)
    print('~' * tam)
    print(c[0], end='')


#Programa principal
comando = ''
while True:
    sleep(1)
    titulo('    SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('    ATÉ LOGO', 2)
