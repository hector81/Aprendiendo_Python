'''
EJERCICIOS MÓDULOS pickle Y json
 2. Recupere el contenido del fichero 'ejercicios.pic' o 'ejercicios.json'.
 Determine el número de líneas que ha programado hasta ahora en el curso.
 No cuentan las líneas en blanco ni las líneas que sean comentarios.
'''
import pickle
import json
#FUNCIONES
def recuperarDatos_modulo_JSON(ruta):
    with open(ruta, 'r') as archivo_entrada:
        objeto = json.load(archivo_entrada)
        objeto_en_json = json.dumps(objeto) # Para volcar el dato en una cadena:
        objeto_load_json = json.loads(objeto_en_json) # Para recuperar el dato desde la cadena
        return objeto_load_json

def numeroLineas_por_FicheroRuta(ruta):
    contador = 0
    try:
        with open(ruta, "r", encoding="utf8") as archivo:
            for linea in archivo.readlines():
                if not "#" in linea[0] and not "'''" in linea[0:3] and len(linea.strip()) > 0:
                    contador += 1

    except FileNotFoundError:
        print("la ruta no es correcta")
    return contador

def numeroTotalLineaArchivos(diccionarioJSON):
    numeroLineasTotal = 0
    numeroLineas = 0
    for key in diccionarioJSON:
        print(f"Archivo = {key} . Ruta absluta = {diccionarioJSON[key]}")
        numeroLineas = numeroLineas_por_FicheroRuta(diccionarioJSON[key])
        print(f"El número de lineas de este archivo es {numeroLineas}")
        numeroLineasTotal += numeroLineas
        numeroLineas = 0
    print(f"**************************")
    print(f"El número total de lineas de todos los archivos es {numeroLineasTotal}")


# VARIABLES
rutaJSON = "C:\\xampp\\htdocs\\AprenderPython\\Ejercicios\\L10_BibliotecaEstandarPython\\modulos_pickle_json\\ejercicios.json"
diccionarioJSON = recuperarDatos_modulo_JSON(rutaJSON)
numeroTotalLineaArchivos(diccionarioJSON)
