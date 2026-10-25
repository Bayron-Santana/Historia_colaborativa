
nombres = ["Tom Cruise", "Hayley Atwell", "Ving Rhames", "Simon Pegg", "Esai Morales"]

edades = {
    "Tom Cruise": 64,
    "Hayley Atwell": 44,
    "Ving Rhames": 67,
    "Simon Pegg": 56,
    "Esai Morales": 64
}

nombre = input("Ingresa un nombre: ")

if nombre in edades:
    print(nombre + " tiene " + str(edades[nombre]) + " años.")
else:
    print("El Agente " + nombre + " no existe en la agencia")
