print('Olá Mundo!')
print('=' * 60)
help(print)
print('=' * 60)
print(input.__doc__)
print('=' * 60)
print(print.__doc__)
print('=' * 60)

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: final da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


#Programa Principal
contador(2, 10, 2)
help(contador)

print('=' * 60)
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


#Programa principal
somar(3, 2, 5)
somar()
somar(1)
somar(2, 3)

print('=' * 60)
def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


#Programa principal
n1 = 2
funcao()
print(f'N1 fora vale {n1}')

print('=' * 60)
def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


#Programa principal
a = 5
print(f'A fora vale {a}')
teste(a)
print('Após chamada da função onde A foi definido como global')
print(f'A fora vale {a}')

print('=' * 60)
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


#Programa principal
r1 = somar(3, 2, 4)
r2 = somar(4, 2, 1)
r3 = somar(2)
r4 = somar(2, 2)
print(f'Os resultados foram {r1}, {r2}, {r3} e {r4}')

print('=' * 60)
def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


#Programa principal
n = int(input("Digite um número: "))
print(f'O fatorial de {n} é', fatorial(n))
