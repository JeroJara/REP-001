'''''
import datetime

hoy = datetime.datetime.now()

semana = ["lun", "mart","wed","jueves","viernes","sabado","domingo"]

print(hoy)

fecha = input("ingrese fecha del vuelo (dia/mes/año): ")
fechasistema = datetime.datetime.strptime(fecha,"%d/%m/%Y")
print(fechasistema)

dia = fechasistema.weekday() 
# if dia<=3: 

print(dia)

print(semana[dia])
'''

ciudades = ["bogota" , "medellin" , "cartagena"]

origen = input("ingrese el origen  ").lower()

if origen in ciudades:
    print(origen.capitalize())