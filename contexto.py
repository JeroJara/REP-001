# Solicitamos al usuario el nombre del archivo a crear
nombre_archivo = input("Ingrese el nombre del archivo de texto: ")

# Usamos 'with' para crear el archivo y escribir datos en él
with open(nombre_archivo, 'w') as archivo:
    # Solicitamos al usuario los datos a escribir en el archivo
    datos = input("Ingrese los datos que desea escribir en el archivo: ")
    datos2 = input("Ingrese la envergadura del A380: " )
    datos3 = bool(input("diga si False O True: "))
    archivo.write(datos+ "\n")
    archivo.write(datos2+ "\n")
    archivo.write(str(datos3)+"\n")

# Ahora usamos 'with' para leer los datos del archivo
with open(nombre_archivo, 'r') as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)