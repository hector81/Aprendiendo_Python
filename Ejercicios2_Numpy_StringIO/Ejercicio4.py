'''
EJERCICIO Kumpula es un barrio de Helsinki, y queremos analizar sus datos de temperatura del mes de junio de 2016.

4. Utilizando matplotlib, visualiza la diferencia MAX-MIN frente a la mínima (matplotlib.pyplot.plot(x, y))
'''
import numpy as np
from io import StringIO
import matplotlib.pyplot as plt

# FUNCIONES
def devolverContenidoTextoArchivo(archivo):
    with open(archivo, "r", encoding="utf8") as archivoLeer:
        textoDevolver = ""
        for linea in archivoLeer.readlines():
            if linea[0] != "#" and linea[0].isdigit() != False:
                textoDevolver = textoDevolver + linea
        return textoDevolver

def devolverListaMaxMinDiferenciasTemp(lista):
    listaMaxMin = []
    diferencia = 0
    #esto es para la maxima
    for dia_temperaturas in lista:
        diferencia = dia_temperaturas[2] - dia_temperaturas[3]
        listaMaxMin.append(diferencia)
    return listaMaxMin

def devolverListaMinimas(lista):
    listaMinimas = []
    for dia_temperaturas in lista:
        listaMinimas.append(dia_temperaturas[3])
    return listaMinimas


# VARIABLES
archivo = "Kumpula-June-2016-w-metadata.txt"

# OPERACIONES
textoDatos = devolverContenidoTextoArchivo(archivo)
textoDatosSTR = StringIO(textoDatos)


listaTuplasTemperaturas = np.genfromtxt(textoDatosSTR, delimiter=',', usecols=[0,1,2,3], dtype=None)
listaDiferenciasMaxMin = devolverListaMaxMinDiferenciasTemp(listaTuplasTemperaturas)
listaMinimas = devolverListaMinimas(listaTuplasTemperaturas)

plt.plot(listaMinimas)
plt.ylabel('Lista de minimas')
plt.show()

plt.plot(listaDiferenciasMaxMin)
plt.xlabel('Lista diferencia Max Min')
plt.show()

plt.plot(listaMinimas ,listaDiferenciasMaxMin)
plt.show()
