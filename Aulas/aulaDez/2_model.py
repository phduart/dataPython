"""
Faremos train_test_split
Treinaremos e testaremos em dados diferentes, assim teremos 
uma estimativa melhor do desempenho dos nossos modelos

Perceba que apesar de usarmos um metodo correto, ele nao e o melhor possivel
"""
# importando bibliotecas e pacotes auxiliares
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.metrics import accuracy_score
from warnings import filterwarnings
filterwarnings('ignore')

# constantes
PATH_FILE_HISTORIC = 'data_split/diabetes_historico.csv'
PATH_FILE_FUTURE = 'data_split/diabetes_futuro.csv'
TEST_SIZE = 0.3
RANDOM_STATE = 42

# leitura dos dados
df_diabetes = pd.read_csv(PATH_FILE_HISTORIC)

# separando entre features e labels
X = df_diabetes.drop(columns='Outcome').to_numpy()
y = df_diabetes.loc[:, 'Outcome'].to_numpy()

# separando entre dados de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE)

# instanciando os modelos
logis_regr = LogisticRegression(random_state=RANDOM_STATE) 
deci_tree = DecisionTreeClassifier(random_state=RANDOM_STATE)
grad_boost = GradientBoostingClassifier(random_state=RANDOM_STATE)
rand_forest = RandomForestClassifier(random_state=RANDOM_STATE)

# lista de tuplas com nomes e modelos
list_models = [('LogisticRegression', logis_regr), ('DecisionTree', deci_tree), ('GradientBoosting', grad_boost), ('RandomForest', rand_forest)]

# treinando os modelos
for model in list_models:
    model[1].fit(X_train, y_train.ravel())

# previsao com os modelos
print('\n')
print('ESTAMOS TREINANDO E TESTANDO EM DADOS DIFERENTES')
for model in list_models:
    y_pred = model[1].predict(X_test)
    print(f'A acurácia do modelo {model[0]} é: {accuracy_score(y_test, y_pred)*100:.2f}%')

# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# leitura de dados que nunca vimos
diabetes_real = pd.read_csv(PATH_FILE_FUTURE)
X_real = diabetes_real.drop(columns='Outcome').to_numpy()
y_real = diabetes_real.loc[:, 'Outcome'].to_numpy()

# treinando nos dados de treino completos
for model in list_models:
    model[1].fit(X, y.ravel())

# previsao com os modelos em dados reais que nunca vimos
print('--------------------------------------')
print('--------------------------------------')
print('ESTAMOS TESTANDO EM DADOS QUE NUNCA VIMOS')
for model in list_models:
    y_pred = model[1].predict(X_real)
    print(f'A acurácia do modelo {model[0]} é: {accuracy_score(y_real, y_pred)*100:.2f}%')
