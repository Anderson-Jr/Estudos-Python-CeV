frase = input('Insira uma expressão: ')
auxiliar = []
for caractere in frase:
    if caractere == '(':
        auxiliar.append('(')
    elif caractere == ')':
        if len(auxiliar) > 0:
            auxiliar.pop()
        else:
            auxiliar.append(')')
if len(auxiliar) > 0:
    print('Expressão incorreta! ')
else:
    print('Expressão correta!')