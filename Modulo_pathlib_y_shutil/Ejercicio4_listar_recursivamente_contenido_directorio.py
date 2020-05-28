
# EJERCICIOS MÓDULO pathlib (Y shutil)
# 4. Liste recursivamente el contenido de su directorio de usuario (C:\Users\alumno).
# Muestre cada ruta en una línea, y etiquete cada una como DIRECTORIO o como FICHERO.
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
        if file_path.is_file():
            print(f"El elemento {archivo} es un FICHERO. Su ruta es {directorio}")
        if file_path.is_dir():
            print(f"**************************************")
            print(f"El elemento {archivo} es un DIRECTORIO")
            nuevoDirectorio = directorio + "/" + str(archivo)
            print(f"***{nuevoDirectorio} . CONTENIDO = **********")
            leerContenidoDirectorio(nuevoDirectorio)
            print(f"**************************************")

# VARIABLES
base_path = Path('.')
# directorio = 'C:/Users/User' carpetaNueva   'C:/carpetaNueva'
directorio = 'C:/Users/User'
# OPERACIONES
leerContenidoDirectorio(directorio)
