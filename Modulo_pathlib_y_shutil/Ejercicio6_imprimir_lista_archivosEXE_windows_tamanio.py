"""
EJERCICIOS MÓDULO pathlib (Y shutil)
6. Realice un listado de ficheros del directorio C:\windows\system32. Almacene
en un fichero llamado "listado_windows.txt" la ruta y tamaño de cada fichero
con el formato siguiente: ruta;tamaño con una línea para cada fichero encontrado.
(Para conocer el tamaño, método stat, atributo st_size)
"""
from pathlib import Path
import glob
import os

# FUNCIONES
def crearListaFicherosExtension(extension, ruta):
    listaFicherosEXE = glob.glob(extension)
    with open(ruta, "w") as archivo:
        for archivoEXE in listaFicherosEXE:
            stat = os.stat(archivoEXE)
            tamanio = stat.st_size
            lista = f"{archivoEXE};{tamanio}\n"
            archivo.writelines(lista)

# VARIABLES
listaArchivosEXE = []
extension = "C:\Windows\system32\\*"
ruta = "listado_windows.txt"
base_path = Path('.')

# OPERACIONES
crearListaFicherosExtension(extension, ruta)
