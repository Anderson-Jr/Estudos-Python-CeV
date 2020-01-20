from datetime import date
ano = int(input('Para saber se o ano atual é bissexto pressione 0. Insira um ano: '))
if ano == 0:
    ano = date.today().year
if ano % 100 == 0 and ano % 400 != 0 or ano % 4 != 0:
    print('O ano não é bissexto!')
else:
    print('O ano é bissexto!')
