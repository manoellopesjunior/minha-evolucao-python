
def notas(*num, sit=False):
    """
    Analisa várias notas e retorna um dicionário com informações.

    Parâmetros:
        *num: uma ou mais notas (números).
        sit: mostra ou não a situação da turma (opcional).

    Retorna:
        Um dicionário contendo:
        - quantidade de notas
        - maior nota
        - menor nota
        - média das notas
        - situação (apenas se sit=True)
    """

    r = dict()
    r["qtd_notas"] = len(num)
    r["maior_nota"] = max(num)
    r["menor_nota"] = min(num)
    r["media"] = sum(num) / len(num)
    if sit:
        if r["media"] >= 8:
            r["situação"] = 'BOA'
        elif  8 > r["media"] >= 5:
            r["situação"] = 'RAZOAVEL'
        elif r["media"] < 5:
            r["situação"] = 'RUIM'
    return r
    

resp = notas(5.5, 2.5, 2, 3.7, sit=True)
print(resp)