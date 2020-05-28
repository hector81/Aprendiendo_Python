"""
EJERCICIOS MÓDULO pathlib (Y shutil)
3. Cree un directorio llamado 'python'. Dentro de ese directorio cree otro
llamado 'texto' y otro llamado 'scripts'. Copie en el directorio 'texto' los
ficheros de su directorio de trabajo que tengan extensión '.txt'. Copie en
el directorio 'scripts' todos aquellos ficheros de su directorio de trabajo
que tengan extensión '.py'.
"""
from pathlib import Path
import shutil
import glob

# FUNCIONES
def crearDirectorios(listaDirectorios):
    directorio = listaDirectorios[0]
    # creamos el directorio
    subdir_path = base_path / directorio
    subdir_path.mkdir(parents=True)
    subdir_path.mkdir(exist_ok=True)
    # creamos los subdirectorios
    subdirectorio = listaDirectorios[1]
    for elemento in subdirectorio:
        nombreRuta = directorio + "/" + elemento
        subdir_path = base_path / nombreRuta
        subdir_path.mkdir(parents=True)
        subdir_path.mkdir(exist_ok=True)

def crearListaFicherosExtension(tipoArchivo):
    listaFicheros = []
    extension = ""
    if tipoArchivo == "texto":
        extension = '*.txt'
    if tipoArchivo == "scripts":
        extension = '*.py'
    ficheros = base_path.glob(extension)
    for elemento in ficheros:
        listaFicheros.append(elemento)
    return listaFicheros

def introducirFicheros_en_directorios(listaDirectorios):
    # creamos los subdirectorios
    subdirectorio = listaDirectorios[1]
    for elemento in subdirectorio:
        nombreRuta = elemento + '\\'
        listaFicheros = crearListaFicherosExtension(elemento)
        for fichero in listaFicheros:
            file_path = base_path / (str(listaDirectorios[0]) + '\\' + str(nombreRuta) + str(fichero))
            my_file = Path(fichero)
            to_file = Path(file_path)
            shutil.copy(my_file, to_file)
# VARIABLES
listaDirectorios = ["python",["texto", "scripts"]]
base_path = Path('.')

# OPERACIONES
crearDirectorios(listaDirectorios)
introducirFicheros_en_directorios(listaDirectorios)
