"""
Nao faremos train_test_split
Treinaremos e testaremos nos mesmos dados
"""
# importando bibliotecas auxiliares
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.metrics import accuracy_score

PATH_FILE = '/Users/pauloduarte/WorkSparcesGit/dataPython/Aulas/aulaDez/diabetes_historico.csv'
RANDOM_STATE = 42

# leitura dos dados
df_diabetes = pd.read_csv(PATH_FILE)

# separando as features e labels
X = df_diabetes.drop(columns='Outcome').to_numpy()
y = df_diabetes.loc[:, 'Outcome'].to_numpy()

# instanciando os modelos que usaremos
logis_regr = LogisticRegression(random_state=RANDOM_STATE) 
deci_tree = DecisionTreeClassifier(random_state=RANDOM_STATE)
grad_boost = GradientBoostingClassifier(random_state=RANDOM_STATE)
rand_forest = RandomForestClassifier(random_state=RANDOM_STATE)

# lista de tuplas com nomes e modelos
list_models = [('LogisticRegression', logis_regr), ('DecisionTree', deci_tree), ('GradientBoosting', grad_boost), ('RandomForest', rand_forest)]

# treinando os modelos
for model in list_models:
    model[1].fit(X, y.ravel())

# previsao com os modelos
# estamos prevendo nos mesmos dados que treinamos
print('\n\n\n')
print('ESTAMOS TREINANDO E TESTANDO NOS MESMOS DADOS - NUNCA FAÇA ISSO!!!!!')
for model in list_models:
    y_pred = model[1].predict(X)
    print(f'A acurácia do modelo {model[0]} é: {accuracy_score(y, y_pred)*100:.2f}%')

# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# leitura de dados que nunca vimos
diabetes_real = pd.read_csv('/Users/pauloduarte/WorkSparcesGit/dataPython/Aulas/aulaDez/diabetes_futuro.csv')
X_real = diabetes_real.drop(columns='Outcome').to_numpy()
y_real = diabetes_real.loc[:, 'Outcome'].to_numpy()

# previsao com os modelos em dados reais que nunca vimos
print('--------------------------------------')
print('--------------------------------------')
print('ESTAMOS TESTANDO EM DADOS QUE NUNCA VIMOS')
for model in list_models:
    y_pred = model[1].predict(X_real)
    print(f'A acurácia do modelo {model[0]} é: {accuracy_score(y_real, y_pred)*100:.2f}%')
