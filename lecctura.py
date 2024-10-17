'''''
fp = open("texto.txt","r")
#Contiene info del archivo
datos = fp.read(3)
print(datos)
datos = fp.read(5)
print(datos)
fp.close()
'''''

'''''
linea = fichero.readlines()
print(linea)
linea = fichero.readline()
print(linea)
print(linea)
fichero.close()
#Lee hasta encontrarse un enter en el texto

'''''
#¿Cómo calcular el número de palabras que tiene una línea?
fichero = open("texto.txt","r")
linea = fichero.readline()
numero_caracteres = len(linea)
print(f"La frase tiene {numero_caracteres} caracteres")
nueva_linea = linea.split()
numero_palabras = len(nueva_linea)
print(numero_palabras)
print(linea)