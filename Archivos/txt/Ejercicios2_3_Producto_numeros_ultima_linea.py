
'''
EJERCICIOS Manipulación de ficheros utilizando el intérprete Fichero "datos_ficheros"
********************************************************
3. El producto de los números de la última línea
********************************************************
'''
# funciones
def producto_numeros_ultima_linea(ruta):
    potenciaTotal = 0
    lineaNum = " "
    with open(ruta, "r", encoding="utf8") as archivo:
        for linea in archivo.readlines():
            lineaSeparacion = linea.split("   ")
            lineaNum = escribir_String_numeros_linea(lineaSeparacion)
            lineaNumMult = escribir_String__multiplicacion_numeros_linea(lineaSeparacion)
            potenciaTotal = escribir_PotenciaTotal(lineaSeparacion)
    print(f"Los numeros serían = {lineaNum}")
    print(f"La multiplicación sería = {lineaNumMult}")
    print(f"El producto sería = {potenciaTotal}")

def escribir_PotenciaTotal(lineaSeparacion):
    potenciaTotal = 1
    for i in range(len(lineaSeparacion)):
        potenciaTotal *= int(lineaSeparacion[i])
    return potenciaTotal

def escribir_String_numeros_linea(lineaSeparacion):
    numero = ""
    lineaNum = ""
    for i in range(len(lineaSeparacion)):
        numero = str(lineaSeparacion[i]) + str(",")
        lineaNum += numero
        numero = ""
    return lineaNum[0:(len(lineaNum) - 1)] # para quitarle el ultimo ,

def escribir_String__multiplicacion_numeros_linea(lineaSeparacion):
    numero = ""
    lineaNumMult = ""
    for i in range(len(lineaSeparacion)):
        numero = str(lineaSeparacion[i]) + str("*")
        lineaNumMult += numero
        numero = ""
    return lineaNumMult[0:(len(lineaNumMult) - 1)] # para quitarle el ultimo *
# variables
rutaEntrada = "datos_fichero.txt"
# operaciones
linea = producto_numeros_ultima_linea(rutaEntrada)
