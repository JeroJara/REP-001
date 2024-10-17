from random import randint

lista = []
for _ in range(5):
    dato = str(randint(0,100))
    lista.append(dato + "  ")
    #_ significa que no se está utilizando esa variable.

##maximo = str(max(lista))
#minimo = str(min(lista))
#prom = str(sum(lista)/len(lista))

file_datos = open("datos.txt","w")
#file_datos.write(maximo)
#file_datos.write("\n")
#file_datos.write(minimo)
#file_datos.write("\n")
##file_datos.write("\n")
file_datos.writelines(lista)
file_datos.close()
print("Archivo creado...")
print(lista)