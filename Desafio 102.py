def fatorial(num, mostra):
    fac = c = 1
    while c <= num:
        fac *= c
        c += 1
    if mostra == True:
        c = 1
        while c < num:
            print(c, end=' x ')
            c += 1
        print(f'{c} = {fac}')
    else:
        print(f'Resultado: {fac}')


#Programa principal.upper()
f = int(input('Digite um valor para ver seu fatorial: '))
calc = input('Deseja ver o desenvolvimento do cálculo? [S/N]')
if calc[0].upper() == 'S':
    fatorial(f, True)
else:
    fatorial(f, False)