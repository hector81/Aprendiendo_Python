'''
EJERCICIO Kumpula es un barrio de Helsinki, y queremos analizar sus datos de temperatura del mes de junio de 2016.

2. Obtener la media de temperatura para las columnas TEMP, MAX, MIN.

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

def devolverTemperaturasMediasDias(lista):
    for dia_temperaturas in lista:
        strDia = str(dia_temperaturas[0])
        fechaStr = strDia[6:8] + "-" + strDia[4:6] + "-" + strDia[0:4]
        temp_media = ((dia_temperaturas[2]+dia_temperaturas[3])/2)
        print(f"La temperaturas del dia {fechaStr} son las siguientes : Mean {dia_temperaturas[1]}. Máxima {dia_temperaturas[2]}. Mínima {dia_temperaturas[3]}. Media {temp_media}")


# VARIABLES
archivo = "Kumpula-June-2016-w-metadata.txt"

# OPERACIONES
textoDatos = devolverContenidoTextoArchivo(archivo)
textoDatosSTR = StringIO(textoDatos)

#dtype=[('myint','i8'),('myfloat','f8'),('mystring','S5')]
listaTuplasTemperaturas = np.genfromtxt(textoDatosSTR, delimiter=',', usecols=[0,1,2,3], dtype=None)
devolverTemperaturasMediasDias(listaTuplasTemperaturas)
