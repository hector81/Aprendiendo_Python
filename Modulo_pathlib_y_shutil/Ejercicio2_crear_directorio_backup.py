"""
EJERCICIOS MÓDULO pathlib (Y shutil)
 2. Realice una copia de seguridad de su directorio de trabajo (donde guarda
sus scripts de Python). La copia será un directorio llamado 'python_backup'.
Si ese directorio existe, pida permiso para actualizarlo. Si lo obtiene, hágalo.
Si no, muestre el mensaje: 'Copia de seguridad abortada'.

"""
from pathlib import Path
import os

# FUNCIONES
def introducirRespuesta():
     while True:
         try:
             respuesta = input(f"Por favor ingrese una respuesta: ")
             if respuesta.upper() == 'S' or respuesta.upper() == 'N':
                 print(f"La respuesta es " + respuesta.upper())
                 return respuesta.upper()
                 break
         except ValueError:
             print(f"Oops! No era válido. Intente nuevamente...")

def crearDirectorio_python_backup(nombreDirectorio):
    # Ruta absoluta
    abs_base_path = base_path.absolute()
    rutaAbsoluta = str(abs_base_path) + '\\' + nombreDirectorio + '\\'
    if os.path.isdir(rutaAbsoluta):
        print('¿La carpeta ya existe. Quiere volver a crearla o actualizarla ? (S/N)')
        respuesta = introducirRespuesta()
        if respuesta.upper() == "S":
            try:
                # creamos el directorio
                subdir_path = base_path / nombreDirectorio
                subdir_path.mkdir(parents=True)
                subdir_path.mkdir(exist_ok=True)
                print(f"Copia de seguridad creada")
            except FileExistsError :
                print(f"No ha dejado crearla porque ya existía")
        elif respuesta.upper() == "N":
            print(f"Copia de seguridad abortada")
    else:
        # creamos el directorio si no existia antes
        subdir_path = base_path / nombreDirectorio
        subdir_path.mkdir(parents=True)
        subdir_path.mkdir(exist_ok=True)
        print(f"Copia de seguridad creada")




# VARIABLES
nombreDirectorio = "python_backup"
base_path = Path('.')

# OPERACIONES
crearDirectorio_python_backup(nombreDirectorio)
