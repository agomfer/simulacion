import generadores
import matplotlib.pyplot as plt
import test
import time


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
   plt.title(title)
   plt.show()


#Definición de parámetros para generador GLC
seed = 2
a = 25214903917
c = 11
m = 2 ** 48

n = 10000
iter = 10

DescGLC = []
FreqsGLC = []
resultGLC = generadores.glc(seed, a, c, m, n)
#graficaFrecuecias(resultGLC,'GLC')
FreqsGLC = test.EstDesc(resultGLC,DescGLC)

test.ChiCuad(FreqsGLC)

time.sleep(10)

DescCuadrado = []
FreqsCuadrado = []
resultCuadrado = generadores.cuadradosmedios(1556,n)
#graficaCuadrado(resultCuadrado[0],resultCuadrado[1],'Cuadrado',iter)
FreqsCuadrado = test.EstDesc(resultCuadrado[1],DescCuadrado)
test.ChiCuad(FreqsCuadrado)


print("PRUEBA DE FRECUENCIA - MÉTODO DE LOS CUADRADOS MEDIOS")
test.pruebaMonobit(resultCuadrado[1])
