
'''
EJERCICIOS Manipulación de ficheros utilizando el intérprete Fichero "datos_ficheros"
********************************************************
1. Guardar en otro fichero de texto una línea con la operación de suma que
 incluya todos los operandos y el resultado, e.g: 24 + 34 + 2 = 60
********************************************************
'''
# funciones
def leerArchivo_lista_numeros_filas(ruta):
    lineaSumaTotal = ""
    with open(ruta, "r", encoding="utf8") as archivo:
        for linea in archivo.readlines():
            lineaSeparacion = linea.split("   ")
            lineaNum = escribir_sumaString_numeros_linea(lineaSeparacion)
            lineaSuma = lineaNum[0:(len(lineaNum) - 2)] # para quitarle el ultimo +
            suma = escribir_sumaTotal_linea(lineaSeparacion)
            lineaSumaTotal = lineaSumaTotal + f"{lineaSuma} = {suma}\n"
    return lineaSumaTotal


def escribirArchivo_suma_numeros_linea(lineaSumaTotal,rutaSalida):
    with open(rutaSalida, "w") as archivo:
        archivo.write(lineaSumaTotal)
    print("Archivo nuevo creado")

def escribir_sumaTotal_linea(lineaSeparacion):
    suma = 0
    numero = 0
    for i in range(len(lineaSeparacion)):
        numero = int(lineaSeparacion[i])
        suma += numero
    return suma

def escribir_sumaString_numeros_linea(lineaSeparacion):
    numero = ""
    lineaNum = ""
    for i in range(len(lineaSeparacion)):
        numero = str(lineaSeparacion[i]) + str(" + ")
        lineaNum += numero
        numero = ""
    return lineaNum





# variables
rutaEntrada = "datos_fichero.txt"
rutaSalida = "datos_fichero_sumas.txt"
# operaciones
lineaSumaTotal = leerArchivo_lista_numeros_filas(rutaEntrada)
print(lineaSumaTotal)
escribirArchivo_suma_numeros_linea(lineaSumaTotal,rutaSalida)
