from time import sleep
def funcao(chamada):
    print('\033[41m=-' * 30)
    print('{:^60}'.format(f'Acessando o Manual do comando {chamada}'))
    print('=-' * 30, '\033[m')
    print(end='\033[1;40m')
    print(help(chamada))

#Programa principal
while True:
    print('\033[45m=-' * 30)
    print('{:^60}'.format('SISTEMA DE AJUDA PyHELP'))
    print('=-' * 30)
    conf = input('\033[mFunção ou biblioteca > ').strip().lower()
    if conf == 'fim':
        break
    funcao(conf)
