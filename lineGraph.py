#Visualização de dados em Python
#import tkinter
import matplotlib.pyplot as plt


x = [1,2,5]
y = [2,3,7]

#Título do Gráfico
plt.title("Meu primeiro Grágico com Python")

#Eixos

plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")


plt.plot(x,y)
plt.show()
