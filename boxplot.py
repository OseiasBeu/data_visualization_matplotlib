#Boxplot - Diagrama de caixas
#Visualização que mostra o quão dispersos estão os meus dados.

import matplotlib.pyplot as plt
import random #Gerar dados aleatórios

#vetor = [1,2,3,4,6,12,551,12,2]

vetor = []

for i in range(10):
    numero_aleatorio = random.randint(0,5)
    vetor.append(numero_aleatorio)

plt.boxplot(vetor)
plt.title("Boxplot")
plt.show()
