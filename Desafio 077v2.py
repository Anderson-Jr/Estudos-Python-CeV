palavras = ('Abacate', 'Abobora', 'Mago', 'Borboleta', 'Desafio', 'Bruno', 'Buccelatti')
for palavra in palavras:
    print(f'\nAs vogais da palavra {palavra} são: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end='')