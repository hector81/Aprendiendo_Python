"""
EJERCICIOS MÓDULO pathlib (Y shutil)
5. Liste todos los archivos ejecutables (extensión '.exe') del directorio C:\Windows\system32.
"""
from pathlib import Path
import os
import glob

# FUNCIONES
def crearListaFicherosExtension(ruta, extension):
    os.chdir(ruta)
    listaFicherosEXE = glob.glob(extension)
    return listaFicherosEXE


# VARIABLES
listaArchivosEXE = []
ruta = "C:\Windows\system32\\"
extension = "*.exe"
base_path = Path('.')

# OPERACIONES
listaArchivosEXE = crearListaFicherosExtension(ruta, extension)
for archivoEXE in listaArchivosEXE:
    print(archivoEXE)
