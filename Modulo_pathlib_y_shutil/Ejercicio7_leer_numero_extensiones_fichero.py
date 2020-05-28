"""
EJERCICIOS MÓDULO pathlib (Y shutil)
7. Liste los ficheros C:\windows\system32 "listado_windows.txt" para determinar
el número de ficheros que tienen igual extensión.
"""
from pathlib import Path
import glob
import os

# FUNCIONES
def leer_devolver_ListaFicheros(ruta):
    listaArchivos = []
    with open("listado_windows.txt", "r") as archivo:
        for linea in archivo.readlines():
            file = linea.split(";") # la linea es ruta;tamaño
            ruta_archivo = file[0] # cogemos solo la ruta_archivo
            ruta_archivo_separados = os.path.split(ruta_archivo) # ahora separamaos ruta de archivo_extension
            print(ruta_archivo_separados[1])
            listaArchivos.append(ruta_archivo_separados[1])
    return listaArchivos

def listaNumero_ListaFicheros(listaArchivos):
    listaExtensiones = []
    contadorCarpetas = 0
    for archivo_extension in listaArchivos:
        lista_archivo_extension = archivo_extension.split(".") # sep
        if len(lista_archivo_extension) == 1: # no tiene extension ,es carpeta
            contadorCarpetas += 1
        elif len(lista_archivo_extension) == 2:
            extension = lista_archivo_extension[1] #sacamos la extension
            listaExtensiones.append(extension)
    #quitamos duplicados
    print(f"")
    print(f"NÚMERO EXTENSIONES")
    listaExtensiones_sin_repeticiones = list(set(listaExtensiones))
    # y contamos repeticiones
    for extension in listaExtensiones_sin_repeticiones:
        print(f"Hay {listaExtensiones.count(extension)} ficheros de la extensión {extension}")
    # y tambien las carpetas
    print(f"Hay {contadorCarpetas} carpetas")

# VARIABLES
listaArchivos = []
ruta = "listado_windows.txt"
base_path = Path('.')

# OPERACIONES
listaArchivos = leer_devolver_ListaFicheros(ruta)
listaNumero_ListaFicheros(listaArchivos)
