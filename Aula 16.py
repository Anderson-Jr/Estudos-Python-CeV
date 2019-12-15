lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim")
print(lanche[3])
print(lanche[1:])
print(lanche[:])
print(lanche[1:3])
for c in lanche:
    print(c)

for contagem in range (0, len(lanche)):
    print("Comida atual: ", lanche[contagem])

print("-----------------")

for pos, comida in enumerate(lanche):
    print(f"Vou comer o lanche {comida} na posição {pos}")

print(sorted(lanche))

a = [2, 5, 4]
b = [5, 8, 1, 2]
c = a + b
print(a)
print(b)
print(c)
print(len(c))
print(c.count(9))
print(c.index(8))
print(c.index(2))
print(c.index(2, 1))

print("--------------")
pessoa = ('Gustavo', 12, 'M', 45.4)
print(pessoa)
print('Apagando pessoa ...')
del(pessoa)
print(pessoa)