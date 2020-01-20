frase = input('Insira uma frase: ').upper().strip()
print("A letra 'a' aparece {} vezes!".format(frase.count('A')))
print('A letra "a" aparece a primeira vez na posição {}'.format(frase.find('A')))
print('A letra "a" aparece a última vez na posição {}'.format(frase.rfind('A')))
