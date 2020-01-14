def getContagemLista(lista):
    return len(lista)

def getSomaLista(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma

def getMediaLista(lista):
    return getSomaLista(lista)/len(lista)

def getDesvioPadrao(lista):
    media = getMediaLista(lista)
    sumDesvio = 0.0
    for i in lista:
        sumDesvio += (i - media)*(i - media)
    return sumDesvio/len(lista)

def getMaxValue(lista):
    lista = sorted(lista)
    return lista[len(lista)-1]

def getMinValue(lista):
    lista = sorted(lista)
    return lista[0]

def getIntervalo(lista):
    return getMaxValue(lista) - getMinValue(lista)

def getCova(feature, target):
    media_feature = getMediaLista(feature)
    media_target = getMediaLista(target)
    diferenca = [(x - media_feature) * (y - media_target) for x, y in zip(feature, target)]
    return getSomaLista(diferenca)