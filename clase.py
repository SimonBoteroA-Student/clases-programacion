nombre = input("INGRESA TU NOMBRE: ")

print("Bienvenida, " + nombre)

edad = 17

print("El nombre es una varianle de tipo: " + str(type(nombre)))
print("La edad es una varianle de tipo: " + str(type(edad)))

edad = str(edad)
nombre = int(nombre)
print("La edad es una varianle de tipo: " + str(type(edad)))

print("La edad de " + nombre + " es " + str(edad))