import pickle
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

precos = ["500", "2000", "5000"]
fim_semana = ["Não", "Sim"]
clima = ["Sol", "Nublado", "Chuva"]
companhia = ["Sozinho", "Acompanhado"]
features = ["Fim de Semana", "Previsão", "Preço", "Companhia"]

print("Preço da viagem: ")
for i, opcao in enumerate(precos):
    print(f"{i+1} - {opcao}")

print("Fim de semana: ")
for i, opcao in enumerate(fim_semana):
    print(f"{i+1} - {opcao}")

print("Clima: ")
for i, opcao in enumerate(clima):
    print(f"{i+1} - {opcao}")

print("Companhia: ")
for i, opcao in enumerate(companhia):
    print(f"{i+1} - {opcao}")

preco_escolhido = int(input("Selecione o preço da viagem: "))
fim_semana_escolhido = int(input("Está planejando viajar no fim de semana? Selecione uma opção: "))
clima_escolhido = int(input("Qual o clima no local de destino? Selecione uma opção: "))
companhia_escolhida = int(input("Está planejando viajar sozinho ou acompanhado? Selecione uma opção: "))

if preco_escolhido < 1 or preco_escolhido > len(precos):
    print("Escolha de preço inválida!")
if fim_semana_escolhido < 1 or fim_semana_escolhido > len(fim_semana):
    print("Escolha de fim de semana inválida!")
if clima_escolhido < 1 or clima_escolhido > len(clima):
    print("Escolha de clima inválida!")
if companhia_escolhida < 1 or companhia_escolhida > len(companhia):
    print("Escolha de acompanhamento inválida!")

dados_usuario = [[ fim_semana_escolhido - 1, clima_escolhido - 1, preco_escolhido - 1, companhia_escolhida - 1]]

dados_usuario_df = pd.DataFrame(dados_usuario, columns=features)

with open("arvore_decisao.pkl", "rb") as f:
    arvore_decisao = pickle.load(f)

resposta = arvore_decisao.predict(dados_usuario_df)

print(f"Você deveria viajar? {resposta[0]}")