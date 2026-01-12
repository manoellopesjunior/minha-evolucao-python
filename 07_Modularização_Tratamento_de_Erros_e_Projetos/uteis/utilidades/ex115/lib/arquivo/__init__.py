from lib.interface import cabecalho

def arquivoexiste(nome):
    """
    Verifica se um arquivo existe.

    Parâmetros:
        nome (str): nome do arquivo a ser verificado.

    Retorno:
        bool: True se o arquivo existir, False caso contrário.
    """
    try:
        a = open(nome, 'rt')  # tenta abrir o arquivo em modo leitura
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criararquivo(nome):
    """
    Cria um arquivo de texto vazio.

    Parâmetros:
        nome (str): nome do arquivo a ser criado.

    Retorno:
        None
    """
    try:
        a = open(nome, 'wt+')  # cria arquivo para escrita (wt+) e leitura
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerarquivo(nome):
    """
    Lê e exibe o conteúdo do arquivo de pessoas cadastradas.

    Parâmetros:
        nome (str): nome do arquivo a ser lido.

    Retorno:
        None
    """
    try:
        a = open(nome, 'rt')  # abre o arquivo para leitura
    except:
        print('ERRO ao ler o arquivo')
    else:
        cabecalho('Pessoas Cadastradas')  # exibe cabeçalho
        for linha in a:
            dado = linha.split(';')  # separa nome e idade
            dado[1] = dado[1].replace('\n', '')  # remove quebra de linha
            print(f'{dado[0]:<30}{dado[1]:>3} anos')  # imprime formatado
    finally:
        a.close()  # garante que o arquivo seja fechado

def cadastrar(arq, nome='desconhecido', idade=0):
    """
    Adiciona um novo registro de pessoa no arquivo.

    Parâmetros:
        arq (str): nome do arquivo onde será gravado.
        nome (str): nome da pessoa a ser cadastrada (padrão: 'desconhecido').
        idade (int): idade da pessoa a ser cadastrada (padrão: 0).

    Retorno:
        None
    """
    try:
        a = open(arq, 'at')  # abre o arquivo em modo append
    except:
        print('Houve um ERRO na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')  # escreve o registro
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
