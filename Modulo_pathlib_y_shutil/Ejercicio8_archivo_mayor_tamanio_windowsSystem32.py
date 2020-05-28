"""
EJERCICIOS MÓDULO pathlib (Y shutil)
8. ¿Cuál es el fichero de mayor tamaño de los registrados en "listado_windows.txt"?
"""
from pathlib import Path
import glob
import os

# FUNCIONES
def devolverFicheroMayor_tamanio(extension):
    tamanioMayor = 0
    archivoMayor = ""
    listaFicherosEXE = glob.glob(extension)
    for archivoEXE in listaFicherosEXE:
        stat = os.stat(archivoEXE)
        tamanioFichero = stat.st_size
        if tamanioFichero > tamanioMayor:
            tamanioMayor = tamanioFichero
            archivoMayor = archivoEXE
    print(f"El archivo '{archivoMayor}' es el que tiene mayor tamaño de los registrados en C:\Windows\system32 con un tamaño de {tamanioMayor}")

def leer_y_sacarFicheroMayor_tamanio(ruta):
    tamanioMayor = 0
    archivoMayor = ""
    listaFicherosEXE = glob.glob(extension)
    with open(ruta, "r") as archivo:
        for linea in archivo.readlines():
            lineaS = linea.split(";")
            tamanioFichero = int(lineaS[1])
            if tamanioFichero > tamanioMayor:
                tamanioMayor = tamanioFichero
                archivoMayor = lineaS[0]

    print(f"El archivo '{archivoMayor}' es el que tiene mayor tamaño de los registrados en C:\Windows\system32 con un tamaño de {tamanioMayor}")

# VARIABLES
listaArchivosEXE = []
extension = "C:\Windows\system32\\*"
base_path = Path('.')
ruta = "listado_windows.txt"
# OPERACIONES
devolverFicheroMayor_tamanio(extension)
leer_y_sacarFicheroMayor_tamanio(ruta)
