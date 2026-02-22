def voto(ano):
    """
    Determina a situação de voto de uma pessoa com base no ano de nascimento.

    Parâmetros:
    ano (int): Ano de nascimento da pessoa.

    Retorno:
    str: Uma mensagem informando a idade calculada e a situação do voto,
         que pode ser:
         - 'NÃO VOTA' (menor de 16 anos)
         - 'VOTO OPCIONAL' (entre 16 e 17 anos ou acima de 65 anos)
         - 'VOTO OBRIGATÓRIO' (entre 18 e 65 anos)

    Regra:
    A idade é calculada com base no ano atual do sistema.
    """
    from datetime import date 
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com idade de {idade} anos: NÃO VOTA'
    elif  16 <= idade < 18 or idade > 65:
        return f'Com idade de {idade} anos: VOTO OPCIONAL' 
    else:
        return f'Com idade de {idade} anos: VOTO OBRIGATÓRIO'


nasc = int(input('Em que ano voçê nasceu:?: '))
print(voto(nasc))
     