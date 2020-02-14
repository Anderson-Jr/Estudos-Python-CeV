resp = dict()
def notas(*n, sit=False):
    """
    -> Analisa notas e situações de alunos
    :param n: Uma ou mais notas dos alunos (aceita quantidades variáveis de nota)
    :param sit: (Opcional) Se deve mostrar ou não mostrar a situação do aluno
    :return: Dicionário com várias informações sobre a situação do aluno
    """
    maior = menor = n[0]
    for nota in n:
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota
    media = sum(n)/len(n)
    resp = {'total': len(n), 'maior': maior, 'menor': menor, 'média': media}
    if sit:
        if media < 0 or media > 10:
            resp['situação'] = 'Foram inseridas notas inválidas'
        elif media < 5:
            resp['situação'] = 'ruim'
        elif media < 7.5:
            resp['situação'] = 'boa'
        elif media < 10:
            resp['situação'] = 'excelente'
    return resp

#Programa principal
resp = notas(-20, 5, 5, sit=True)
print(resp)
