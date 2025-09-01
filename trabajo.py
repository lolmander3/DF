# Programa para clasificar nivel de hemoglobina

# Entrada de datos
genero = int(input("Ingrese su género (1: Hombre, 2: Mujer): "))
hemoglobina = float(input("Ingrese el nivel de hemoglobina: "))

# Proceso y salida
if genero == 1:  # Hombre
    if hemoglobina < 12.2:
        print("Baja")
    elif hemoglobina <= 16.6:
        print("Normal")
    else:
        print("Alta")

elif genero == 2:  # Mujer
    if hemoglobina < 12.6:
        print("Baja")
    elif hemoglobina <= 15:
        print("Normal")
    else:
        print("Alta")

else:
    print("No es posible generar la alerta")
