#funcion que recibe cantidad de datos float y rango de valores; y retorna una lista
# funcón que recibe una lista y calcula el promedio y la desviacion estándar.
#  función que calcula cuántos datos están por encima del promedio; y cuáles son esos datos.
from random import uniform #para generar numeros aleatorios tipo float
from math import sqrt
#########################################################################################################################
def crea_lista_float(cantidad:int, liminferior:float, limsuperior:float):
    #1. Crear la lista vacía a llenar con datos
    aleatoriosfloat = []
    #2. Utilizo un bucle 
    for i in range(cantidad):
        #3. Genro un número aleatorio
        numero = uniform(liminferior,limsuperior)
        #4. Agrego el número a la lista
        aleatoriosfloat.append(numero)
        #5. Se retorna el dato.
    return aleatoriosfloat

# funcion que recibe una lista y calcula el promedio y la desviacion estándar
def estadisticas(datos:list):
    prom = sum(datos)/len(datos)
    #ahora la desviacion estandar:
    suma = 0
    for Xi in datos:
        suma += (Xi-prom)**2
    termino = suma/len(datos)
    desviacion_estandar = sqrt(termino)
    return prom, desviacion_estandar
# función que calcula cuántos datos están por encima del promedio; y cuáles son esos datos

def buenpromedio(lista:list, promedio:float):
    contador = 0
    datosmayor = []
    for dato in lista:
        if dato > promedio:
            contador += 1
            datosmayor.append(dato)
    return contador, datosmayor
########################################################################################################################
#programa principal:
#LISTA ALEATORIOS
lista_aleatorios = crea_lista_float(100,10.0,20.0)
print(lista_aleatorios)
#PROMEDIO Y DESVIACION ESTANDAR
promedio, desviacion = estadisticas(lista_aleatorios)
print (f"PRomedio = {promedio},Desviacion Estándar = {desviacion}")
#DATOS MAYORES
cantidadmayores, lista_mejores = buenpromedio(lista_aleatorios,promedio)
print(f"La cantidad de notas sobre el promedio fue de {cantidadmayores} y fueron {lista_mejores}")


