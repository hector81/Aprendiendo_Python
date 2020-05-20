'''
EJERCICIO Kumpula es un barrio de Helsinki, y queremos analizar sus datos de temperatura del mes de junio de 2016.

1. Utilizar la función np.genfromtxt para cargar el contenido del
archivo Kumpula-June-2016-wmetadata.txt (necesitaremos especificar el delimitador de campos
y que hay que evitar las primeras filas de cabecera del fichero).
'''
import numpy as np
from io import StringIO

# FUNCIONES
def devolverContenidoTextoArchivo(archivo):
    with open(archivo, "r", encoding="utf8") as archivoLeer:
        textoDevolver = ""
        for linea in archivoLeer.readlines():
            if linea[0] != "#" and linea[0].isdigit() != False:
                textoDevolver = textoDevolver + linea
        return textoDevolver

# VARIABLES
archivo = "Kumpula-June-2016-w-metadata.txt"

# OPERACIONES
textoDatos = devolverContenidoTextoArchivo(archivo)
textoDatosSTR = StringIO(textoDatos)

data1 = np.genfromtxt(textoDatosSTR, dtype=[('myint','i8'),('myfloat','f8'),('mystring','S5')], delimiter=",")
print(data1)
