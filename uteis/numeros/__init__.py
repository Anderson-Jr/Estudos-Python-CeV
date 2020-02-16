def dobro(n=0, formato=False):
    """
    -> Calucla o dobro de um valor
    :param n: Valor a ser dobrado
    :return: Dobro de n
    """
    res = n * 2
    return res if formato is False else moeda(res)


def triplo(n=0, formato=False):
    """
    -> Calcula o triplo de um valor
    :param n: Valor a ser triplicado
    :return: O triplo de n
    """
    res = n * 3
    return res if formato is False else moeda(res)


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


def metade(n=0, formato=False):
    """
    -> Calcula a metade do número
    :param n: Número a ser dividido por 2
    :return: A metade de n
    """
    res = n/2
    return res if formato is False else moeda(res)


def aumentar(n=0, porc=0, formato=False):
    """
    -> Calcula uma porcentagem de aumento para n
    :param n: Valor a ser aumentado
    :param porc: Porcentagem para aumentar o valor
    :return: O valor n após sofrer um aumento de porc% (por cento)
    """
    n *= (1 + porc / 100)
    res = round(n, 2)
    return res if formato is False else moeda(res)


def diminuir(n=0, porc=0, formato=False):
    """
    -> Diminui uma porcentagem de n
    :param n: Valor a ser diminuído
    :param porc: porcentagem para diminuir de n
    :param formato: Se o valor de n deve ser formatado para algum tipo de moeda (Ex: 100 -> R$100,00 ou U$100,00)
    :return: Retorna o valor de n após diminuído
    """
    n -= (n * porc/100)
    res = round(n, 2)
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    """
    -> Manipula números
    :param preco: Valor
    :param moeda: Moeda a ser considerada
    :return: Simbolo da Moeda + valor
    """
    return f'{moeda}{preco}'.replace('.', ',')


def resumo(preco, aumento=10, reducao=5):
    """
    -> Faz um resumo do preço de um produto
    :param preco: Valor do produto
    :param aumento: Porcentagem de aumento
    :param reducao: POrcentagem de redução
    :return: Tabela detalhada dos preços
    """
    print('=-' * 15)
    print('RESUMO DO VALOR'.center(30))
    print('=-' * 15)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preco, aumento, True)}')
    print(f'{reducao}% de redução: \t{diminuir(preco, reducao, True)}')
    print('=-' * 15)
