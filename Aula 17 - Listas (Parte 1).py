lanche = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim']
print(lanche)
print(lanche[2])
print(lanche[3])
lanche[3] = 'Picolé'
print(lanche[3])
lanche.append('Cookie') #Adiciona um elemento no final da lista
lanche.insert(0, 'Cachorro-Quente') #Adiciona outro elemento em um lugar específico mas sem apagar o outro
del lanche[3]
lanche.pop() #Remove o último elemento
lanche.pop(2)
lanche.remove('Hambúrguer') #Indicar o valor/conteúdo a ser eliminado
if 'Pizza' in lanche:
    lanche.remove('Pizza') #Nessa forma, elimina apenas a primeira ocorrência do parâmetro citado
print(lanche)
print('='*30)
valores = list(range(0, 11)) #Elementos dentro de uma lista através de range
print(valores)
valores.append(0.4)
valores.sort()
print(valores)
valores.sort(reverse=True)
print(valores)
len(valores)
print('='*40)
num = [2, 5, 9, 1]
num[2] = 3
print(num)
num.append(7)
num.insert(2, 0)
print(num)
print('='*30)
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
for pos, valor in enumerate(valores):
    print(f'Na posição {pos} há o valor {valor}... ')
print('Fim da lista')
print('='*30)
for c in range (0, 6):
    valores.append(int(input('Digite um valor: ')))
print(valores)
print('='*30)
a = [2, 3, 4, 7]
b = a #Quando uma lista é atribuída a outra, as duas permanecem ligadas entre si
print(f'Lista a: {a}')
print(f'Lista b: {b}')
print('Modificação na lista a')
a[3] = 4
print(f'Lista a: {a}')
print(f'Lista b: {b}')
