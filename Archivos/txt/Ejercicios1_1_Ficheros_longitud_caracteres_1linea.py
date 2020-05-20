'''
EJERCICIOS Manipulación de ficheros utilizando el intérprete Fichero "datos_ficheros"
********************************************************
1. ¿La longitud en caracteres de la primera línea?
********************************************************
'''
# funciones
def leer_y_devolver_primera_linea(ruta):
    linea = ""
    with open(ruta, "r", encoding="utf8") as archivo:
        linea = archivo.readline()
    return linea

def longitud_caracteres_primera_linea(linea1):
    print(linea1)
    print(f"Numero caracteres de la primera línea con espacios en blanco = {len(linea1)}")
    caracteres = linea1.split("   ")
    contadorCaracterSinBlanco = 0
    for palabra in caracteres:
        contadorCaracterSinBlanco += len(palabra)
    print(f"Numero caracteres de la primera línea sin espacios en blanco = {(contadorCaracterSinBlanco-1)}")
    print(f"Tamaño de cada palabra")
    for palabra in caracteres:
        print(f"Palabra = {palabra} . Tamaño = {len(palabra)}")

# variables
ruta = "datos_fichero.txt"
# operaciones
linea1 = leer_y_devolver_primera_linea(ruta)
longitud_caracteres_primera_linea(linea1)
