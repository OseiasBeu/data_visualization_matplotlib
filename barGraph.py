import matplotlib.pyplot as plt

x = [1,2,3,4,5] #quantidade de barras
y = [2,3,7,1,0] #tamanho das barras

titulo = "Gráfico de Barras"
eixox = "Eixo X"
eixoy = "Eixo Y"

#Legendas
plt.title(titulo)
plt.xlabel = (eixox)
plt.ylabel = (eixoy)


plt.bar(x,y)
#plt.show()

plt.savefig("barGraph.svg")
