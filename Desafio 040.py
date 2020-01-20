nota1 = float(input('Enter your first grade: '))
nota2 = float(input('Enter your second grade: '))
average = (nota1 + nota2) / 2
if average < 0:
    print('Invalid average!')
elif average < 5:
    print('You are disapproved!')
elif average < 7:
    print('You are recovering/recuperation!')
elif average <= 10:
    print('you are approved!')
else:
    print('Invalid average!')