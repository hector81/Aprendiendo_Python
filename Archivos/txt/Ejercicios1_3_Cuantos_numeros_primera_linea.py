'''
EJERCICIOS Manipulación de ficheros utilizando el intérprete Fichero "datos_ficheros"
********************************************************
3. ¿Cuántos números contiene la primera línea del fichero?
********************************************************
'''
# funciones
def leer_y_devolver_primera_linea(ruta):
    linea = ""
    with open(ruta, "r", encoding="utf8") as archivo:
        linea = archivo.readline()
    return linea

def devolverNum_numeros_primera_linea(linea1):
    contadorNum = 0
    primer_linea = linea1.split("   ")
    for numeros in primer_linea:
        if numeros.isdigit() == True:
            contadorNum += 1
    print(f"Numero de números en la primera línea = {(contadorNum)}")

# variables
ruta = "datos_fichero.txt"
# operaciones
linea1 = leer_y_devolver_primera_linea(ruta)
devolverNum_numeros_primera_linea(linea1)
