import statistic as st
import pandas as pd

data = pd.read_csv('/Users/pauloduarte/JQ_Academy/Datas/iris.txt')
 
def start():
    while True:
        print(data.describe())
        print()

        hashColunas = {1: 'sepal_length', 2: 'sepal_width', 3: 'petal_length', 4: 'petal_length', 5: 'petal_width'}
        colunas(hashColunas)
        lista = hashColunas[int(input("Escolha uma das colunas: "))]
        print()

        print(f"Contagem        : {st.getContagemLista(data[lista])}")
        print(f"Minimo          : {st.getMinValue(data[lista])}")
        print(f"Maximo          : {st.getMaxValue(data[lista])}")
        print(f"Intervalo       : {st.getIntervalo(data[lista])}")
        print(f"Soma            : {st.getSomaLista(data[lista])}")
        print(f"Media           : {st.getMediaLista(data[lista])}")
        print(f"Desvio Padrão   : {st.getDesvioPadrao(data[lista])}")
        print()

        continuar = input("Deseja continuar? y/n: ")
        if(continuar == 'n' or continuar == 'N'):
            break

def colunas(hashColunas):
    for i in range(1, len(hashColunas)):
        print(f"{i} - {hashColunas.get(i)}")
