'''
EJERCICIOS Manipulación de ficheros utilizando el intérprete Fichero "datos_ficheros"
********************************************************
4. Guardar la suma de los números de la primera línea en otro fichero
********************************************************
'''
# funciones
def leer_y_devolver_primera_linea(ruta):
    linea = ""
    with open(ruta, "r", encoding="utf8") as archivo:
        linea = archivo.readline()
    return linea

def devolverSuma_primera_linea(linea1):
    suma = 0
    primer_linea = linea1.split("   ")
    for numeros in primer_linea:
        if numeros.isdigit() == True:
            suma += int(numeros)
    print(f"Suma de los números en la primera línea = {(suma)}")

# variables
ruta = "datos_fichero.txt"
# operaciones
linea1 = leer_y_devolver_primera_linea(ruta)
devolverSuma_primera_linea(linea1)
