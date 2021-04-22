import generadores
import matplotlib.pyplot as plt



# Definición de gráficas de frecuencias
def graficaFrecuecias(result,title):
   plt.hist(result, bins=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
   plt.grid(True)
   plt.title(title)
   plt.show()

def graficaCuadrado(seeds,values,title,n):
   fig, ax = plt.subplots(1, 1)
   data = []
   for i in range (n):
      data.append([i+1,seeds[i],values[i]])
   print(data)
   column_labels = ["Iteraciones", "seeds", "values"]
   ax.axis('tight')
   ax.axis('off')
   ax.table(cellText=data, colLabels=column_labels, loc="center")
   plt.show()


#Definición de parámetros para generadores
seed = 2
a = 25214903917
c = 11
m = 2 ** 48

resultGLC = generadores.glc(seed, a, c, m, 100)
graficaFrecuecias(resultGLC,'GLC')

resultCuadrado = generadores.cuadradosmedios(1234,100)
graficaCuadrado(resultCuadrado[0],resultCuadrado[1],'Cuadrado',10)