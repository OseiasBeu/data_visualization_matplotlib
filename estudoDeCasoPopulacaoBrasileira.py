#Crescimento da População Brasileira 1980-2016
#DataSus
 
import matplotlib.pyplot as plt

dados = open("populacao-brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.plot(x,y, color='k', linestyle='--')
plt.bar(x,y, color="#e4e4e4")
#plt.scatter(x,y)

plt.title("Crescimento da População Brasileira 1980-2016")
plt.xlabel("ANO:")
plt.ylabel("POPULAÇÃO: x100.000.000")

plt.show()
