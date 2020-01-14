def contagem(lista):
    """
    Conta a quantidade de itens em uma lista
    Parametros
    ----------
    lista: list python - lista que queremos contar os itens

    Returns
    ----------
    Scalar int com a quantidade de itens de uma lista
    """
    cont = 0
    for i in lista:
        cont += 1

    return cont


def minimo(lista):
    """
    Acha o menor valor de uma lista 
    Parametros
    ----------
    lista: list python - lista que queremos saber o menor valor

    Returns
    ----------
    Scalar com o menor valor de uma lista
    """
    minimo = lista[0]
    for item in lista:
        if item < minimo:
            minimo = item

    return minimo


def maximo(lista):
    """
    Acha o maior valor de uma lista 
    Parametros
    ----------
    lista: list python - lista que queremos saber o maior valor

    Returns
    ----------
    Scalar com o maior valor de uma lista
    """
    maximo = lista[0]
    for item in lista:
        if item > maximo:
            maximo = item  

    return maximo


def intervalo(lista):
    """
    Acha o intervalo - diferença entre o maior e menor valor
    de uma lista Python
    Parametros
    ----------
    lista: list python - lista que queremos saber o intervalo

    Returns
    ----------
    Scalar com o valor do intervalo de uma lista
    """
    inter = maximo(lista) - minimo(lista)

    return inter    


def raiz(radicando, indice):
    """
    Acha a raiz n-esima de um numero qualquer
    Parametros
    ----------
    radicando: numero que queremos achar a raiz n-esima
    indice: indice da operacao de radiciacao

    Returns
    ----------
    Scalar com o valor da raiz n-esima de um numero
    """
    resultado = radicando ** (1/indice)

    return resultado


def soma_lista(lista):
    """
    Acha a soma dos elementos de uma lista
    Parametros
    ----------
    lista: list python - lista que queremos saber a soma dos itens

    Returns
    ----------
    Scalar com a soma dos itens de uma lista
    """
    soma = 0
    for i in lista:
        soma += i

    return soma


def media_lista(lista):
    """
    Acha a media aritmetica de uma lista
    Parametros
    ----------
    lista: list python - lista que queremos saber a media aritmetica 
    dos itens

    Returns
    ----------
    Scalar com a media dos itens de uma lista
    """
    media = soma_lista(lista) / contagem(lista)

    return media


def variancia(lista):
    """
    Acha a variancia dos itens de uma lista
    Parametros
    ----------
    lista: list python - lista que queremos saber a variancia 
    dos itens

    Returns
    ----------
    Scalar com a variancia dos itens de uma lista
    """
    media = media_lista(lista)
    tamanho = contagem(lista)    

    diff_dos_quadrados = [(x-media) ** 2 for x in lista]

    soma = soma_lista(diff_dos_quadrados)

    var = soma / (tamanho - 1)

    return var


def desvio_padrao_lista(lista):
    '''
    Acha o desvio padrao dos itens de uma lista
    Parametros
    ----------
    lista: list python - lista que queremos saber o desvio padrao
    dos itens

    Returns
    ----------
    Scalar com o desvio padrao dos itens de uma lista
    '''
    var = variancia(lista)
    std = raiz(var, 2)

    return std


def cova(feature_1, feature_2, media_1, media_2):
    """
    Acha a covariancia entre duas variaveis
    Parametros
    ----------
    feature: lista de valores das features
    target: lista de valores dos targets

    Returns
    ----------
    Scalar com a covariancia
    """
    diferenca = [(x - media_1) * (y - media_2) for x, y in zip(feature_1, feature_2)]
    cov = soma_lista(diferenca) / (contagem(feature_1) - 1)
    
    return cov
 