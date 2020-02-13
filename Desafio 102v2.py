def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: Número a ser calculado
    :param show: Mostrar ou não a conta
    :return: O valor do fatorial do número n
    """
    f = 1
    for c in range(n, 0, -1):
        if show: #ou "if show == true:"
            if c > 1:
                print(f'{c} x', end=' ')
            else:
                print(f'{c} = {f}')
        f *= c
    return f

#Programa principal
print(fatorial(5, show=False))