expressao = input('Insira uma expressão: ')
teste = []
for simbolo in expressao:
    if simbolo == '(':
        teste.append('(')
    elif simbolo == ')':
        if len(teste) > 0:
            teste.pop()
        else:
            teste.append(')')
if len(teste) == 0:
    print('Expressão correta!')
else:
    print('Expressão incorreta!')
