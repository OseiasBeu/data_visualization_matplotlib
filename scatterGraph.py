import matplotlib.pyplot as plt

x = [1,3,5,7,9]
y = [2,3,7,1,0]

titulo = "Scatterplot: Gráfico de Dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)


plt.scatter(x,y, label= "Grupo 1", color= "r")
plt.plot(x,y)
plt.legend()
plt.show()
