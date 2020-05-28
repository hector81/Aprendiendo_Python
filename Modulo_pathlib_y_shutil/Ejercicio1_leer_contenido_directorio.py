"""
EJERCICIOS MÓDULO pathlib (Y shutil)
1. Script que lea el contenido de cualquier directorio que se le pase como parámetro.
Muestre su contenido por pantalla (cada elemento en una línea).
"""
from pathlib import Path
import glob
import os

# FUNCIONES
def leerContenidoDirectorio(directorio):
    os.chdir(directorio)
    contenidoDirectorio = glob.glob("*")
    for elemento in contenidoDirectorio:
        archivo = elemento
        rutaComprobar = str(directorio) + "/" + archivo
        file_path = base_path / rutaComprobar
        print(f"{archivo} . FICHERO = {file_path.is_file()} . DIRECTORIO = {file_path.is_dir()}")

# VARIABLES
base_path = Path('.')
directorio = 'C:/xampp'
# OPERACIONES
leerContenidoDirectorio(directorio)
