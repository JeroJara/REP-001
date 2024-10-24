import matplotlib.pyplot as plt
from random import randint
import random
import math
#Datos
 
time = []
y = []
frecuencia = 30

# y = sin(2*pi*(1/t))

for i in range(frecuencia):
    dato = i/frecuencia
    time.append(dato)

for i in range(frecuencia):
    #x.append(randint(100,200))
    datoY = math.sin(2*math.pi*time[i])
    y.append(datoY)


#Crear la gráfica
plt.plot(time,y)
#Agregar titulo y etiquetas

plt.title("Gráfica de líneas")
plt.xlabel("Tiempo")
plt.xlabel("sin(t)")

#Mostrar gráfica 
plt.show