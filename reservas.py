from random import randint
from modulo import registro
from os import system
system("ls")
invocativo = str(input("¿Cómo desea que nos dirijamos a usted? ¿Señor o Señora?:  "))
nombre = str(input(("Por favor, ingrese su nombre: ")))
apellido = str(input("Por favor, ingrese su apellido:   "))
registro(invocativo,nombre,apellido)

ciudades = ["medellín","bogotá","cartagena"]
dias_semana = ["lunes","martes","miércoles","jueves"]
dias_finde = ["viernes","sábado","domingo"]

origen = str(input("Por favor ingrese su ciudad de origen (Medellín, Bogotá o Cartagena ):  "))
if origen.lower() in ciudades:
    destino = str(input("Por favor ingrese la ciudad de destino:  "))
    if destino.lower() in ciudades and destino != origen:

        dia_semana2 = str(input("Por favor ingrese el día de la semana que desea viajar (De lunes a domingo):  "))
        
        if dia_semana2.lower() in dias_semana:
            if (origen.lower() == "bogotá" and destino.lower() == "medellín") or (origen.lower() == "medellín" and destino.lower() == "bogotá"):
                distance = 240
                price = 79900
            
            elif (origen.lower() == "bogotá" and destino.lower() == "cartagena") or (origen.lower() == "cartagena" and destino.lower() == "bogotá"):
                distance = 657
                price = 156900
            
            elif (origen.lower() == "medellín" and destino.lower() == "cartagena") or (origen.lower() == "cartagena" and destino.lower() == "medellín"):
                distance = 461
                price = 156900
            else:
                print("Destino no válido")
        


        elif dia_semana2.lower() in dias_finde:
            if (origen.lower() == "bogotá" and destino.lower() == "medellín") or (origen.lower() == "medellín" and destino.lower() == "bogotá"):
                distance = 240
                price = 119900
            
            elif (origen.lower() == "bogotá" and destino.lower() == "cartagena") or (origen.lower() == "cartagena" and destino.lower() == "bogotá"):
                distance = 657
                price = 213000
            
            elif (origen.lower() == "medellín" and destino.lower() == "cartagena") or (origen.lower() == "cartagena" and destino.lower() == "medellín"):
                distance = 461
                price = 213000

            else:
                print("Destino no válido")
        
        else:
            print("Día de la semana no válido")
    
    else:
        print("Destino no puede ser igual al origen o ciudad no válida")
 


preferencia = str(input("¿Dónde prefiere sentarse? (Pasillo, Ventana, sin preferencia):  "))

def asiento(preferencia):
    if preferencia.lower() == "pasillo":
        asiento_pasajero = "C"
    elif preferencia.lower() == "ventana":
        asiento_pasajero = "A"
    else:
        asiento_pasajero = 'B'
    
    numero = randint(1,29)
    return numero,asiento_pasajero


dia_mes = int(input("Por favor escriba el día del mes que desea viajar (1 al 30):  "))
mes = str(input("¿Qué mes desea viajar?:  "))


print(f"Tu vuelo de {origen} a {destino} el día {dia_mes} de ¨{mes.lower()} está reservado ")
print(f"El precio de boleto es {price}")
print(f"Su asiento es {asiento(preferencia)}")


###