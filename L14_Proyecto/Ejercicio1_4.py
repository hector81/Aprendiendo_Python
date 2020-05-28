'''
 4. Generar una carpeta de salida 'Mensuales'
'''
import os


def crearCarpetaSalida(nombre):
    try:
        os.mkdir(nombre)
        print(f"Carpeta {nombre} creada")
    except OSError:
        print(f"La carpeta {nombre} ya existe en est directorio")


nombre = "Mensuales"
crearCarpetaSalida(nombre)
