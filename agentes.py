
nombres = [
    "Tom Cruise",
    "Hayley Atwell",
    "Ving Rhames",
    "Simon Pegg",
    "Esai Morales",
    "Henry Cavill",
    "Rebecca Ferguson",
    "Vanessa Kirby",
    "Jeremy Renner",
    "Angela Bassett"
]

edades = {
    "Tom Cruise": 64,
    "Hayley Atwell": 44,
    "Ving Rhames": 67,
    "Simon Pegg": 56,
    "Esai Morales": 64,
    "Henry Cavill": 43,
    "Rebecca Ferguson": 42,
    "Vanessa Kirby": 38,
    "Jeremy Renner": 55,
    "Angela Bassett": 68
}

nombre = input("Ingresa un nombre: ")

if nombre in edades:
    print(nombre + " tiene " + str(edades[nombre]) + " años.")
else:
    print("El Agente " + nombre + " no existe en la agencia")
