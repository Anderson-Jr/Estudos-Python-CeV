print('{:=^40}'.format(' Radar eletrônico '))
velocidade = float(input('Qual a velocidade do veículo em km/h? '))
print('='*40)
if velocidade > 80:
    multa = (velocidade-80)*7
    print(f'Você foi multado em R${multa:.2f}')
else:
    print('Pode seguir viagem! Não ultrapasse os 80km/h!!')
print('=' * 40)