'''def login(numero_repeticion):
    print("Esta es la repeticion numero "+ str(numero_repeticion))
    nombre = input("Cual es tu nombre? --> ")
    edad = int(input("Cual es tu edad? --> "))

    if edad > 18:
        print(nombre + ", eres mayor de edad")
    elif edad == 18:
        print(nombre + ", tienes 18 años")
    else:
        print(nombre + ", eres menor de edad")

repeticiones = int(input("Cuantos logins deseas hacer? --> "))

for repeticion in range(repeticiones):
    login(repeticion)'''


tabla = int(input("Ingrese el numero de la tabla de multiplicar: "))
for numero in range(1, 12):
    resultado = tabla * numero
    print("" + str(tabla) + " x " + str(numero) + " = " + str(resultado))
