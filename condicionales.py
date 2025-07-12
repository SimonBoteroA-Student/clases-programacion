nombre = input("Cual es tu nombre? --> ")
edad = int(input("Cual es tu edad? --> "))

if edad > 18:
    print(nombre + ", eres mayor de edad")
elif edad == 18:
    print(nombre + ", tienes 18 años")
else:
    print(nombre + ", eres menor de edad")