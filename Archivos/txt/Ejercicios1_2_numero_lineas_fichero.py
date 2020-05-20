'''
EJERCICIOS Manipulación de ficheros utilizando el intérprete Fichero "datos_ficheros"
********************************************************
2. El número de líneas del fichero
********************************************************
'''
# funciones
def devolver_numero_lineas_fichero(ruta):
    numLineas = 0
    with open(ruta, "r", encoding="utf8") as archivo:
        for linea in archivo.readlines():
            numLineas += 1
    print(f'Número de lineas del fichero = {numLineas}')

# variables
ruta = "datos_fichero.txt"
# operaciones
devolver_numero_lineas_fichero(ruta)
