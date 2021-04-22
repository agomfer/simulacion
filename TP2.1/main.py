import generadores
import matplotlib.pyplot as plt



# Definición de gráficas de frecuencias
def graficaFrecuecias(result):
   plt.hist(result, bins=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
   plt.grid(True)
   plt.show()

#Definición de parámetros para generadores
seed = 2
a = 25214903917
c = 11
m = 2 ** 48

resultGLC = generadores.glc(seed, a, c, m, 100000)
graficaFrecuecias(resultGLC)