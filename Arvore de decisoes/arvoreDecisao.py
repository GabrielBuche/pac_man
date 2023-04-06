from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
import pandas as pd
import pickle

auxData = pd.read_csv('dados.csv')
data = auxData.drop(columns=['Carimbo de data/hora'])

data['Fim de Semana'] = data['Fim de Semana'].replace({'NÃO': 0, 'SIM': 1})
data['Previsão'] = data['Previsão'].replace({'SOL': 0, 'NUBLADO': 1, 'CHUVA': 2})
data['Preço'] = data['Preço'].replace({500: 0, 2000: 1, 5000: 2})
data['Companhia'] = data['Companhia'].replace({'SOZINHO': 0, 'ACOMPANHADO': 1})

# Separa a coluna "viajar" do dados para ser analizado
X = data.drop('Viajar', axis=1)
y = data['Viajar']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

arvoreDecisao = DecisionTreeClassifier()

arvoreDecisao.fit(X_train, y_train)

with open("arvore_decisao.pkl", "wb") as f:
    pickle.dump(arvoreDecisao, f)

tree.plot_tree(arvoreDecisao)
plt.show()

