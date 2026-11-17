#diagnostico por ia
#risco de infarto
#arvore de decisão
 
#bibliotecas
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
 
 
#dados ficticios
 
x = [
    [25, 120, 80],
    [65, 170, 110],
    [45, 140, 95],
    [70, 180, 120],
]
 
y = [0, 1, 0, 1]
 
#definiçao do modelo
modelo = DecisionTreeClassifier()
 
#treinamento do modelo
modelo.fit(x, y)
 
#contadores de risco
baixo_risco = 0 
alto_risco = 0
 
#quantidade de pacientes 
qtd = int(input("Quantos pacientes deseja analisar? "))
 
#analise dos pacientes
 
for i in range(qtd):
 
    print(f"\npaciente {i+1}")
 
    idade = int(input("Idade: "))
    pressao = int(input("Pressao arterial: "))
    freq = int(input("frequencia cardiaca: "))
 
    paciente = [[idade, pressao, freq]]
 
    resultado = modelo.predict(paciente)
 
    if resultado[0] == 1: 
      print("classificaçao: alto risco")
      alto_risco += 1
    else:
      print("classificaçao: baixo risco")
      baixo_risco += 1