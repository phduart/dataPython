def somaLista(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma

def mediaList(lista):
    return somaLista/len(lista)

def getDesvioPadrao(lista):
    mediaLista = mediaList(lista)
    sumDesvio = 0.0
    for i in lista:
        sumDesvio += (i - mediaLista)*(i - mediaLista)
    return sumDesvio/len(lista)
