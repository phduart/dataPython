import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

from sklearn.metrics import classification_report, accuracy_score

RANDOM_SEED = 42

modelLogistic = LogisticRegression(random_state=RANDOM_SEED)
modelDecision = DecisionTreeClassifier(random_state=RANDOM_SEED)
modelRandomForest = DecisionTreeClassifier(random_state=RANDOM_SEED)
modelGradientBoosting = GradientBoostingClassifier(random_state=RANDOM_SEED)

modelos = [ ('modelLogistic',modelLogistic), 
            ('modelDecision', modelDecision), 
            ('modelRandomForest', modelRandomForest), 
            ('modelGradientBoosting', modelGradientBoosting) ]

df = pd.read_csv('/Users/pauloduarte/WorkSparcesGit/dataPython/Aulas/aulaDez/diabetes_historico.csv')

X = df.drop(columns=['Outcome'])
y = df.loc[:, 'Outcome']

for model in modelos:
    model[1].fit(X, y)
    

print(df.head())
print(df['Glucose'].mean())
print(df['Glucose'].median())
print(df['Glucose'].std())

