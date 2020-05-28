'''
EJERCICIOS MÓDULOS pickle Y json
1. Haga un listado de todos los ficheros con extensión .py de su directorio de trabajo.
Almacénelos en un diccionario que tendrá como claves los nombres de los ficheros y
como valor, la ruta absoluta en el disco. Guarde este diccionario en un fichero
 llamado 'ejercicios.pkl' haciendo uso del módulo pickle, y en un
 fichero 'ejercicios.json' haciendo uso del módulo json.
'''
import pickle
import json
from pathlib import Path
# FUNCIONES
def devolverFicheroArchivoRuta(ruta):
    return [obj.name for obj in Path(ruta).iterdir() if obj.is_file()]

def crearListadoFicherosExtensionPy(ruta):
    listadoFicheros = []
    archivos = devolverFicheroArchivoRuta(ruta)
    for archivo in archivos:
        if archivo[len(archivo)-3:len(archivo)] == '.py':
            listadoFicheros.append(archivo)
    return listadoFicheros

def crearDiccionarioRutasAbsolutas(ruta, listasArchivos):
    diccionarioRutasAbs = {}
    for elemento in listasArchivos:
        diccionarioRutasAbs[elemento] = ruta + "\\" + elemento
    return diccionarioRutasAbs

def guardarDiccionario_modulo_pickle(diccionarioRutasAbsolutas):
    with open('ejercicios.pkl', 'wb') as archivo_salida:
         pickle.dump(diccionarioRutasAbsolutas, archivo_salida)

def guardarDiccionario_modulo_JSON(diccionarioRutasAbsolutas):
    with open('ejercicios.json', 'w') as archivo_salida:
         json.dump(diccionarioRutasAbsolutas, archivo_salida)


# VARIABLES
ruta = "C:\\xampp\\htdocs\\AprenderPython\\Ejercicios\\L10_BibliotecaEstandarPython\\modulos_pickle_json"
listasArchivos = crearListadoFicherosExtensionPy(ruta)
diccionarioRutasAbsolutas = crearDiccionarioRutasAbsolutas(ruta, listasArchivos)
guardarDiccionario_modulo_pickle(diccionarioRutasAbsolutas)
guardarDiccionario_modulo_JSON(diccionarioRutasAbsolutas)
