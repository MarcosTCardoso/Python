def notas(*n, sit=False):
    """
    -> Programa cria dicionário com situação da turma.
    :param n: Vai receber as notas de uma turma
    :param sit: Parâmetro opcional, que se True informa a situaçao da turma.
    :return: Retorna o dicionário com dados da turma.
    By Marcos Cardoso
    """
    dados = {'total': len(n), 'maior': max(n), 'menor': min(n), 'média': sum(n) / len(n)}
    situação = ''
    if sit:
        if dados['média'] >= 7:
            situação = 'Boa'
        elif dados['média'] >= 5:
            situação = 'Regular'
        else:
            situação = 'Ruim'
    if situação != '':
        dados['situação'] = situação
    return dados


resp = notas(3.5, 7.2, 8, 9, sit=True)
print(resp)
help(notas)
