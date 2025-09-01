# Inicializar contadores
hBaja = hNormal = hAlta = 0
mBaja = mNormal = mAlta = 0

N = int(input("Cantidad de pacientes: "))

for i in range(N):
    genero = int(input("Genero (1=Hombre, 2=Mujer): "))
    hb = float(input("Hemoglobina: "))

    if genero == 1:  # Hombre
        if hb < 12.2:
            hBaja += 1
        elif hb <= 16.6:
            hNormal += 1
            else:
            hAlta += 1
    else:  # Mujer
        if hb < 12.6:
            mBaja += 1
        elif hb <= 15:
            mNormal += 1
        else:
            mAlta += 1

# Mostrar resultados
print("Hombres Baja:", hBaja)
print("Hombres Normal:", hNormal)
print("Hombres Alta:", hAlta)
print("Mujeres Baja:", mBaja)
print("Mujeres Normal:", mNormal)
print("Mujeres Alta:", mAlta)

