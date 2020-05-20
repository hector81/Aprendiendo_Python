
'''
EJERCICIOS Manipulación de ficheros utilizando el intérprete Fichero "datos_ficheros"
********************************************************
5. La suma de todos los números impares del document
********************************************************
'''
# funciones
def leerArchivo_lista_numeros_filas(ruta):
    sumaTotal = 0
    with open(ruta, "r", encoding="utf8") as archivo:
        for linea in archivo.readlines():
            lineaSeparacion = linea.split("   ")
            lineaNumImpar = escribir_sumaString_numeros_impares_linea(lineaSeparacion)
            sumaImpares = suma_impares_linea(lineaSeparacion)
            print(f"{lineaNumImpar[0:(len(lineaNumImpar) - 2)]} . Suma de la línea = {sumaImpares}")
            sumaTotal = sumaTotal + sumaImpares
    print(f"Total suma impares archivo = {sumaTotal}")

def suma_impares_linea(lineaSeparacion):
    suma = 0
    numero = 0
    for i in range(len(lineaSeparacion)):
        numero = int(lineaSeparacion[i])
        if numero%2 != 0:
            suma += numero
    return suma

def escribir_sumaString_numeros_impares_linea(lineaSeparacion):
    numero = ""
    lineaNum = ""
    for i in range(len(lineaSeparacion)):
        numeroInt = int(lineaSeparacion[i])
        if numeroInt%2 != 0:
            numero = str(lineaSeparacion[i]) + str(" + ")
            lineaNum += numero
            numero = ""
    return lineaNum

# variables
rutaEntrada = "datos_fichero.txt"
# operaciones
leerArchivo_lista_numeros_filas(rutaEntrada)
