def notas(*n, sit=False):
    """
    -> Analisa notas e situações de alunos
    :param n: Uma ou mais notas dos alunos (aceita quantidades variáveis de nota)
    :param sit: (Opcional) Se deve mostrar ou não mostrar a situação do aluno
    :return: Dicionário com várias informações sobre a situação do aluno
    """
    resp = {'total': len(n), 'maior': max(n), 'menor': min(n), 'média': sum(n)/len(n)}
    if sit:
        if resp['média'] > 10 or resp['média'] < 0:
            resp['situação'] = 'Foram inseridas notas inválidas'
        elif resp['média'] < 5:
            resp['situação'] = 'ruim'
        elif resp['média'] < 7.5:
            resp['situação'] = 'boa'
        elif resp['média'] < 10:
            resp['situação'] = 'excelente'
    return resp


#Programa principal
resp = notas(-20, 5, 5, sit=True)
print(resp)
