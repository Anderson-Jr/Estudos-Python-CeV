expressao = input('Digite uma expressão: ')
parenteses = list()
for termo in expressao:
    if termo == '(':
        parenteses.append('(')
    elif termo == ')' and (len(parenteses) == 0):
        parenteses.append(')')
    elif termo == ')':
        parenteses.pop()
if len(parenteses) > 0:
    print('Expressão inválida!!')
else:
    print(('Expressão válida!'))