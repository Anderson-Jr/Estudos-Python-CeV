def lin():
   print('-' * 30)


# Programa principal
lin()
print('	Curso em Vídeo ')
lin()
lin()
print('   Learn Python   ')
lin()
lin()
print('	GUSTAVO GUANABARA ')
lin()
print('#' * 30)

def mensagem(msg):
   print('-' * 30)
   print(msg)
   print('-' * 30)


#Programa principal 2
mensagem('Curso em Vídeo')
mensagem('Pythonzinho')
mensagem('Estudo Python')
print('#' * 30)


#Parte prática da aula
def soma(a, b):
   print(f'A = {a} B = {b}')
   s = a + b
   print(f'A soma de {a} + {b} = {s}')


#Programa principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(4, 1)
soma(a=4, b=5)
soma(b=2, a=3)
print('#' * 30)


def contador(*num):
   print(f'Foram passados {len(num)} parâmetros')
   for numero in num:
      print(f'{numero}', end=' ')
   print('... Soma dos valores:', sum(num))


#Programa principal
contador(1, 2, 3)
contador(1, 3)
contador(9, 3, 1, 4)
contador(1)


def dobrar(lista):
   for pos, numero in enumerate(lista):
      lista[pos] *= 2


#Programa principal
numeros = [1, 2, 4, 3, 44, 6, 3]
dobrar(numeros)
print('Sua lista com os valores dobrados é: ', numeros)
