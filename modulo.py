def registro(invocativo,nombre,apellido):
    if invocativo.lower() == "señor" or invocativo.lower() == "señora":
        return print("¡Gracias por elegirnos! Bienvenido a la mejor Aerolínea del barrio, ",invocativo, nombre, apellido)
    else:
        print("Género no válido")


