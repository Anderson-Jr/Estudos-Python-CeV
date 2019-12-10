palavras = ['Útero', 'Ressurreição', 'Febo', 'Sebo', 'Desafio', 'Puzzle']
for palavra in palavras:
    print(f'As vogais da palavra {palavra} são: ', end='')
    for letra in palavra:
        if letra.lower() in 'áàaeéèiìíoóuúù':
            print(letra, end=' ')
    print()
