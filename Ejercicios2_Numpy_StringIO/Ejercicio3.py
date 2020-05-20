'''
EJERCICIO Kumpula es un barrio de Helsinki, y queremos analizar sus datos de temperatura del mes de junio de 2016.

3. ¿Cuál es la mayor diferencia de temperaturas (i.e. MAX - MIN) que se ha producido en un día? ¿Y la mínima?
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

def devolverMayorMinimaDiferenciaTemp(lista):
    diferenciaTempMax = 0
    diferencia = 0
    diaMayor = 0
    #esto es para la maxima
    for dia_temperaturas in lista:
        diferencia = dia_temperaturas[2] - dia_temperaturas[3]
        if diferencia > diferenciaTempMax:
            diferenciaTempMax = diferencia
            diaMayor = dia_temperaturas[0]
            diferencia = 0
    strDia = str(diaMayor)
    fechaStr = strDia[6:8] + "-" + strDia[4:6] + "-" + strDia[0:4]
    print(f"El día con mayor diferencia de temperaturas fue el dia {fechaStr} con una diferencia de {diferenciaTempMax}")

    diferenciaTempMin = diferenciaTempMax
    diaMenor = 0
    #esto es para la maxima
    for dia_temperaturas in lista:
        diferencia = dia_temperaturas[2] - dia_temperaturas[3]
        if diferencia < diferenciaTempMin:
            diferenciaTempMin = diferencia
            diaMenor = dia_temperaturas[0]
            diferencia = 0
    strDia1 = str(diaMenor)
    fechaStr1 = strDia1[6:8] + "-" + strDia1[4:6] + "-" + strDia1[0:4]
    print(f"El día con menor diferencia de temperaturas fue el dia {fechaStr1} con una diferencia de {diferenciaTempMin}")


# VARIABLES
archivo = "Kumpula-June-2016-w-metadata.txt"

# OPERACIONES
textoDatos = devolverContenidoTextoArchivo(archivo)
textoDatosSTR = StringIO(textoDatos)

#dtype=[('myint','i8'),('myfloat','f8'),('mystring','S5')]
listaTuplasTemperaturas = np.genfromtxt(textoDatosSTR, delimiter=',', usecols=[0,1,2,3], dtype=None)
devolverMayorMinimaDiferenciaTemp(listaTuplasTemperaturas)
