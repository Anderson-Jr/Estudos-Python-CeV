def voto(nasc):
    from datetime import date
    idade = date.today().year - nasc
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        return 'Voto negado'
    elif idade < 18 or idade > 65:
        return 'Voto opcional'
    else:
        return 'Voto obrigatório'


#Programa principal
anonasc = int(input('Insira o ano do seu nascimento: '))
print(voto(anonasc))
