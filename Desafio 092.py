from datetime import date
situacao = {'Nome': input('Digite seu nome: '),
            'Idade': date.today().year - int(input('Ano de nascimento: ')),
            'CTPS': int(input('Carteira de trabalho (0 se não possuir): '))}
if situacao['CTPS'] != 0:
    situacao['Contratação'] = int(input('Ano de contratação: '))
    situacao['Salário'] = float(input('Digite seu salário: '))
    situacao['Aposentadoria'] = situacao['Idade'] + 35
print('-=' * 30)
for k, v in situacao.items():
    print(f'{k} tem o valor {v}')