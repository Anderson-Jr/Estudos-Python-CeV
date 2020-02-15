def dobro(n=0):
    """
    -> Calucla o dobro de um valor
    :param n: Valor a ser dobrado
    :return: Dobro de n
    """
    return n * 2


def triplo(n=0):
    """
    -> Calcula o triplo de um valor
    :param n: Valor a ser triplicado
    :return: O triplo de n
    """
    return n * 3


def fatorial(n=0):
    """
    -> Calcula o fatorial de n
    :param n: Valor a ter o fatorial calculado
    :return: fatorial de n
    """
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


def metade(n=0):
    """
    -> Calcula a metade do número
    :param n: Número a ser dividido por 2
    :return: A metade de n
    """
    return n/2


def aumento(n=0, porc=0):
    """
    -> Calcula uma porcentagem de aumento para n
    :param n: Valor a ser aumentado
    :param porc: Porcentagem para aumentar o valor
    :return: O valor n após sofrer um aumento de porc% (por cento)
    """
    n *= (1 + porc / 100)
    n = round(n, 2)
    return n


def moeda(preco=0, moeda='R$'):
    """
    -> Manipula números
    :param preco: Valor
    :param moeda: Moeda a ser considerada
    :return: Simbolo da Moeda + valor
    """
    return f'{moeda}{preco}'.replace('.', ',')